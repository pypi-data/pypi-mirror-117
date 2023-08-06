import torch

from gradsflow.utility.common import (
    module_to_cls_index,
    download,
    get_file_extension,
    get_files,
    listify,
)


def test_create_module_index():
    assert isinstance(module_to_cls_index(torch.optim), dict)


def test_get_files():
    assert len(get_files("./")) != 0


def test_get_file_extension():
    assert get_file_extension("image.1.png") == "png"


def test_download():
    assert "gradsflow" in (download("README.md")).lower()


def test_listify():
    assert listify(None) == []
    assert listify(1) == [1]
    assert listify((1, 2)) == [1, 2]
