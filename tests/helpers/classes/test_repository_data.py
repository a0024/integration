from custom_components.hacs.helpers.classes.repositorydata import RepositoryData


def test_guarded():
    data = RepositoryData.create_from_dict({"full_name": "test"})
    assert data.name == "test"

    data.update_data({"name": "new"})
    assert data.name != "new"
