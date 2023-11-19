import pytest

from org_chart import build_org_chart, max_depth


# Test case for a simple organization
@pytest.mark.parametrize(
    "org_data, expected_depth",
    [
        (["CEO", None, None], 1),
        (["CEO", "VP", None], 2),
        (["CEO", "VP", "Manager", None, None, "Employee", "John"], 3),
    ],
)
def test_simple_organization(org_data, expected_depth):
    org_structure = build_org_chart(org_data)
    depth = max_depth(org_structure)
    assert depth == expected_depth


# Test case for a deeper organization structure
@pytest.mark.parametrize(
    "org_data, expected_depth",
    [
        (["CEO", None, None], 1),
        (["CEO", None, "VP"], 2),
        (["CEO", "VP", "Manager", None, None, "Employee", "John"], 3),
        (["CEO", "CFO", "COO", "EVP", "SVP", None, None, "VP", "Manager"], 4),
        (
            [
                "CEO",
                "CFO",
                "COO",
                None,
                None,
                "VP1",
                "VP2",
                "CTO",
                "Manager1",
                "Manager2",
                "Employee1",
                "Employee2",
                "Employee3",
                "Employee4",
            ],
            5,
        ),
    ],
)
def test_complex_organization(org_data, expected_depth):
    org_structure = build_org_chart(org_data)
    depth = max_depth(org_structure)
    assert depth == expected_depth


# Test case for a very lopsided organization
@pytest.mark.parametrize(
    "org_data, expected_depth",
    [
        (["CEO", "CFO", "COO", "EVP", "SVP", None, None, "VP", "Manager"], 4),
        (
            [
                "CEO",
                "CFO",
                "COO",
                None,
                None,
                "VP1",
                "VP2",
                "CTO",
                "Manager1",
                "Manager2",
                "Employee1",
                "Employee2",
                "Employee3",
                "Employee4",
            ],
            5,
        ),
    ],
)
def test_very_lopsided_organization(org_data, expected_depth):
    org_structure = build_org_chart(org_data)
    depth = max_depth(org_structure)
    assert depth == expected_depth