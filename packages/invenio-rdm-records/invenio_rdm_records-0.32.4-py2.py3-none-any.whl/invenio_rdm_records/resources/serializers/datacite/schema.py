# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""DataCite based Schema for Invenio RDM Records."""

from edtf import parse_edtf
from edtf.parser.grammar import ParseException
from flask import current_app
from flask_babelex import lazy_gettext as _
from invenio_access.permissions import system_identity
from invenio_records_resources.proxies import current_service_registry
from invenio_vocabularies.proxies import current_service as vocabulary_service
from marshmallow import Schema, ValidationError, fields, missing, post_dump, \
    validate
from marshmallow_utils.fields import SanitizedUnicode
from marshmallow_utils.html import strip_html

from invenio_rdm_records.resources.serializers.ui.schema import \
    current_default_locale

from ..utils import get_vocabulary_props


def get_scheme_datacite(scheme, labels):
    """Returns the datacite equivalent of a scheme."""
    return current_app.config[labels][scheme].get("datacite", scheme)


class PersonOrOrgSchema43(Schema):
    """Creator/contributor common schema for v4."""

    name = fields.Str(attribute="person_or_org.name")
    nameType = fields.Method('get_name_type', attribute="person_or_org.type")
    givenName = fields.Str(attribute="person_or_org.given_name")
    familyName = fields.Str(attribute="person_or_org.family_name")
    nameIdentifiers = fields.Method('get_name_identifiers')
    affiliation = fields.Method('get_affiliation')

    def get_name_type(self, obj):
        """Get name type."""
        return obj["person_or_org"]["type"].title()

    def get_name_identifiers(self, obj):
        """Get name identifier list."""
        serialized_identifiers = []
        identifiers = obj["person_or_org"].get("identifiers", [])

        for identifier in identifiers:
            name_id = {
                "nameIdentifier": identifier["identifier"],
                "nameIdentifierScheme": get_scheme_datacite(
                    identifier["scheme"],
                    "RDM_RECORDS_PERSONORG_SCHEMES"
                ),
            }
            serialized_identifiers.append(name_id)

        return serialized_identifiers

    def get_affiliation(self, obj):
        """Get affiliation list."""
        affiliations = obj.get("affiliations", [])

        if not affiliations:
            return missing

        serialized_affiliations = []
        ids = []

        for affiliation in affiliations:
            id_ = affiliation.get("id")
            if id_:
                ids.append(id_)
            else:
                # if no id, name is mandatory
                serialized_affiliations.append(
                    {"name": affiliation["name"]}
                )

        if ids:
            affiliations_service = (
                current_service_registry.get("rdm-affiliations")
            )
            affiliations = affiliations_service.read_many(system_identity, ids)

            for affiliation in affiliations:
                aff = {
                    "name": affiliation["name"],
                }
                identifier = affiliation.get("identifiers")
                if identifier:
                    # PIDS-FIXME: DataCite accepts only one, how to decide
                    identifier = identifier[0]
                    aff["affiliationIdentifier"] = identifier["identifier"]
                    aff["affiliationIdentifierScheme"] = get_scheme_datacite(
                        identifier["scheme"],
                        "VOCABULARIES_AFFILIATION_SCHEMES"
                    ).upper()
                    # upper() is fine since this field is free text. It
                    # saves us from having to modify invenio-vocabularies
                    # or do config overrides.

                serialized_affiliations.append(aff)

        return serialized_affiliations

    @post_dump(pass_many=False)
    def capitalize_name_type(self, data, **kwargs):
        """Capitalize type."""
        if data.get("nameType"):
            data["nameType"] = data["nameType"].capitalize()

        return data


class CreatorSchema43(PersonOrOrgSchema43):
    """Creator schema for v4."""


class ContributorSchema43(PersonOrOrgSchema43):
    """Contributor schema for v43."""

    contributorType = fields.Method('get_role')

    def get_role(self, obj):
        """Get datacite role."""
        role = obj.get("role")
        if not role:
            return missing

        props = get_vocabulary_props(
            'contributorsroles', ['props.datacite'], role["id"])
        return props.get('datacite', '')


class SubjectSchema43(Schema):
    """Subjects schema for v43."""

    subject = fields.Str(attribute="subject")
    valueURI = fields.Str(attribute="identifier")
    subjectScheme = fields.Str(attribute="scheme")


class FundingSchema43(Schema):
    """Funding schema for v43."""

    funderName = fields.Str(attribute="funder.name")
    funderIdentifier = fields.Str(attribute="funder.identifier")
    funderIdentifierType = fields.Method('get_identifier_type')
    awardTitle = fields.Str(attribute="award.title")
    awardNumber = fields.Str(attribute="award.number")
    # PIDS-FIXME: URI should be processed depending on the schema
    awardURI = fields.Str(attribute="award.identifier")

    TO_FUNDER_IDENTIFIER_TYPES = {
        "ISNI": "ISNI",
        "GRID": "GRID",
        "ROR": "ROR",
        "CROSSREF FUNDER ID": "Crossref Funder ID",
        "OTHER": "Other",
    }

    def get_identifier_type(self, obj):
        """Upper case the type."""
        # TODO: Likely has to be revisted when the form support deposit.
        id_type = obj.get("funder", {}).get("scheme", "Other")
        key = id_type.upper()
        return self.TO_FUNDER_IDENTIFIER_TYPES.get(key, "Other")


class DataCite43Schema(Schema):
    """DataCite JSON 4.3 Marshmallow Schema."""

    # PIDS-FIXME: What about versioning links and related ids
    types = fields.Method('get_type')
    titles = fields.Method('get_titles')
    creators = fields.List(
        fields.Nested(CreatorSchema43), attribute='metadata.creators')
    contributors = fields.List(
        fields.Nested(ContributorSchema43), attribute='metadata.contributors')
    publisher = fields.Str(attribute='metadata.publisher')
    publicationYear = fields.Method("get_publication_year")
    subjects = fields.Method("get_subjects")
    dates = fields.Method('get_dates')
    language = fields.Method('get_language')
    identifiers = fields.Method('get_identifiers')
    relatedIdentifiers = fields.Method('get_related_identifiers')
    sizes = fields.List(SanitizedUnicode(), attribute="metadata.sizes")
    formats = fields.List(SanitizedUnicode(), attribute="metadata.formats")
    version = SanitizedUnicode(attribute="metadata.version")
    rightsList = fields.Method('get_rights')
    descriptions = fields.Method('get_descriptions')
    geoLocations = fields.Method("get_locations")
    fundingReferences = fields.List(
        fields.Nested(FundingSchema43), attribute='metadata.funding')
    schemaVersion = fields.Constant("http://datacite.org/schema/kernel-4")

    def get_type(self, obj):
        """Get resource type."""
        props = get_vocabulary_props(
            'resourcetypes',
            ['props.datacite_general', 'props.datacite_type'],
            obj["metadata"]["resource_type"]["id"],
        )
        return {
            'resourceTypeGeneral': props.get("datacite_general", "Other"),
            'resourceType': props.get("datacite_type", ""),
        }

    def _merge_main_and_additional(self, obj, field, default_type=None):
        """Return merged list of main + additional titles/descriptions."""
        result = []
        main_value = obj["metadata"].get(field)

        if main_value:
            item = {field: strip_html(main_value)}
            if default_type:
                item[f"{field}Type"] = default_type
            result.append(item)

        additional_values = obj["metadata"].get(f"additional_{field}s", [])
        for v in additional_values:
            item = {field: strip_html(v.get(field))}

            # Type
            type_id = v.get("type", {}).get("id")
            if type_id:
                props = get_vocabulary_props(
                    f"{field}types", ["props.datacite"], type_id)
                if "datacite" in props:
                    item[f"{field}Type"] = props["datacite"]

            # Language
            lang_id = v.get("lang", {}).get("id")
            if lang_id:
                item["lang"] = lang_id

            result.append(item)

        return result or missing

    def get_titles(self, obj):
        """Get titles list."""
        return self._merge_main_and_additional(obj, "title")

    def get_descriptions(self, obj):
        """Get descriptions list."""
        return self._merge_main_and_additional(
            obj, "description", default_type="Abstract"
        )

    def get_publication_year(self, obj):
        """Get publication year from edtf date."""
        try:
            publication_date = obj["metadata"]["publication_date"]
            parsed_date = parse_edtf(publication_date)
            return str(parsed_date.lower_strict().tm_year)
        except ParseException:
            # Should not fail since it was validated at service schema
            current_app.logger.error("Error parsing publication_date field for"
                                     f"record {obj['metadata']}")
            raise ValidationError(_("Invalid publication date value."))

    def get_dates(self, obj):
        """Get dates."""
        dates = [{
            "date": obj["metadata"]["publication_date"],
            "dateType": "Issued"
        }]

        for date in obj["metadata"].get("dates", []):
            date_type_id = date.get("type", {}).get("id")
            props = get_vocabulary_props(
                'datetypes', ["props.datacite"], date_type_id)
            to_append = {
                "date": date["date"],
                "dateType": props.get("datacite", "Other")
            }
            desc = date.get("description")
            if desc:
                to_append["dateInformation"] = desc

            dates.append(to_append)

        return dates or missing

    def get_language(self, obj):
        """Get language."""
        languages = obj["metadata"].get("languages", [])
        if languages:
            # DataCite support only one language, so we take the first.
            return languages[0]["id"]

        return missing

    def get_identifiers(self, obj):
        """Get (main and alternate) identifiers list."""
        serialized_identifiers = []

        # pids go first so the DOI from the record is the main doi
        # otherwise a doi from identifiers can be used
        pids = obj["pids"]
        for scheme, id_ in pids.items():
            serialized_identifiers.append({
                "identifier": id_["identifier"],
                "identifierType": get_scheme_datacite(
                    scheme, "RDM_RECORDS_IDENTIFIERS_SCHEMES"
                )
            })

        # Identifiers field
        identifiers = obj["metadata"].get("identifiers", [])
        for id_ in identifiers:
            serialized_identifiers.append({
                "identifier": id_["identifier"],
                "identifierType": get_scheme_datacite(
                    id_["scheme"], "RDM_RECORDS_IDENTIFIERS_SCHEMES"
                )
            })

        return serialized_identifiers or missing

    def get_related_identifiers(self, obj):
        """Get related identifiers."""
        serialized_identifiers = []
        metadata = obj["metadata"]
        identifiers = metadata.get("related_identifiers", [])
        for rel_id in identifiers:
            relation_type_id = rel_id.get("relation_type", {}).get("id")
            props = get_vocabulary_props(
                "relationtypes", ["props.datacite"], relation_type_id)
            serialized_identifier = {
                "relatedIdentifier": rel_id["identifier"],
                "relationType": props.get("datacite", ""),
                "relatedIdentifierType": get_scheme_datacite(
                    rel_id["scheme"], "RDM_RECORDS_IDENTIFIERS_SCHEMES"
                )
            }

            resource_type_id = rel_id.get("resource_type", {}).get("id")
            if resource_type_id:
                props = get_vocabulary_props(
                    "resourcetypes",
                    # Cache is on both keys so query datacite_type as well
                    # even though it's not accessed.
                    ["props.datacite_general", "props.datacite_type"],
                    resource_type_id
                )
                serialized_identifier["resourceTypeGeneral"] = props.get(
                    "datacite_general", "Other")

            serialized_identifiers.append(serialized_identifier)

        return serialized_identifiers or missing

    def get_locations(self, obj):
        """Get locations."""
        locations = []

        loc_list = obj["metadata"].get("locations", {}).get("features", [])
        for location in loc_list:
            place = location.get("place")
            serialized_location = {}
            if place:
                serialized_location["geoLocationPlace"] = place
            geometry = location.get("geometry")
            if geometry:
                geo_type = geometry["type"]
                # PIDS-FIXME: Scalable enough?
                # PIDS-FIXME: Implement Box and Polygon serialization
                if geo_type == "Point":
                    serialized_location["geoLocationPoint"] = {
                        "pointLatitude": geometry["coordinates"][0],
                        "pointLongitude": geometry["coordinates"][1],
                    }

            locations.append(serialized_location)
        return locations or missing

    def get_subjects(self, obj):
        """Get datacite subjects."""
        subjects = obj["metadata"].get("subjects", [])
        if not subjects:
            return missing

        serialized_subjects = []
        ids = []
        for subject in subjects:
            sub_text = subject.get("subject")
            if sub_text:
                serialized_subjects.append({"subject": sub_text})
            else:
                ids.append(subject.get("id"))

        if ids:
            subjects_service = (
                current_service_registry.get("rdm-subjects")
            )
            subjects = subjects_service.read_many(system_identity, ids)
            validator = validate.URL()
            for subject in subjects:
                serialized_subj = {
                    "subject": subject.get("subject"),
                    "subjectScheme": subject.get("scheme"),
                }
                id_ = subject.get("id")

                try:
                    validator(id_)
                    serialized_subj["valueURI"] = id_
                except ValidationError:
                    pass

                serialized_subjects.append(serialized_subj)

        return serialized_subjects if serialized_subjects else missing

    def get_rights(self, obj):
        """Get datacite rigths."""
        rights = obj["metadata"].get("rights", [])
        if not rights:
            return missing

        serialized_rights = []
        ids = []
        for right in rights:
            _id = right.get("id")
            if _id:
                ids.append(_id)
            else:
                serialized_right = {
                    "rights": right.get("title").get(
                        current_default_locale()
                    ),
                }

                link = right.get("link")
                if link:
                    serialized_right["rightsUri"] = link

                serialized_rights.append(serialized_right)

        if ids:
            rights = vocabulary_service.read_many(
                system_identity, "licenses", ids
            )
            for right in rights:
                serialized_right = {
                    "rights": right.get("title").get(
                            current_default_locale()
                        ),
                    "rightsIdentifierScheme": right.get("props").get("scheme"),
                    "rightsIdentifier": right.get("id"),
                }
                link = right.get("props").get("url")
                if link:
                    serialized_right["rightsUri"] = link

                serialized_rights.append(serialized_right)

        return serialized_rights if serialized_rights else missing
