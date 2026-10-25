from agent.reviewer import validate

STACK = 'resource "aws_s3_bucket" "logs" {}\n'
HEADINGS = (
    "**What it is:**\n**Why it matters:**\n"
    "**How it could be abused:**\n**How to fix it:**\n"
)


def test_existing_resource_is_clean():
    assert validate(HEADINGS + "Fix `aws_s3_bucket.logs`.", STACK) == []


def test_invented_resource_is_flagged():
    problems = validate(HEADINGS + "Use `aws_kms_key.logs_key`.", STACK)
    assert problems == ["references unknown resource: aws_kms_key.logs_key"]


def test_new_resource_is_allowed():
    text = HEADINGS + "Add a new `aws_s3_bucket_versioning.logs`."
    assert validate(text, STACK) == []


def test_missing_heading_is_flagged():
    assert any("missing heading" in p for p in validate("no headings", STACK))


def test_eg_abbreviation_does_not_hide_new():
    text = HEADINGS + (
        "Add a lifecycle rule (this would be a new resource, "
        "e.g. `aws_s3_bucket_lifecycle_configuration.logs`) so versions expire."
    )
    assert validate(text, STACK) == []


def test_eg_does_not_excuse_invented_reference():
    text = HEADINGS + "Use the existing key, e.g. `aws_kms_key.logs_key`, for this."
    assert validate(text, STACK) == [
        "references unknown resource: aws_kms_key.logs_key"
    ]