# -*- coding: utf-8 -*-

"""Framwork for getting filetype-specific metadata.

Instantiate appropriate calss with filename. Returned object acts like a
dictionary, with key-value pairs for each piece of metadata.
import fileinfo
inof = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
pritn "\\n".join(["%s=%s"% (k, v) for k, v in info.items()])

Or use listDirectory function to get info on all files in a directory.
    for info in fileinfo.listDirectory("/music/ap/",[".mp3"]):
        ...
Framework can be extended by adding classes for particular file types, e.g.
HTMLFileInfo, MPGFileInfo, DOCFileInfo.Each class is completely responsible for
parsing its files appropriately; see MP3FileInfo for example.
"""
import os
import sys
from UserDict import UserDict   #类似于字典的类，允许创建子类


def stripnulls(data):
    """strip whitspace and nulls"""
    return data.replace("\00", "").strip()


class FileInfo(UserDict):
    """stor file metadata"""

    def __init__(self, filename=None):
        super(FileInfo, self).__init__()
        # 用super内置函数的好处是，python自动找到父类
        self["name"] = filename  # key:value


class MP3FileInfo(FileInfo):
    """store ID3v1.0 MP3 tags"""
    tagDataMap = {
        "title": (3, 33, stripnulls),
        "artist": (33, 63, stripnulls),
        "album": (63, 93, stripnulls),
        "year": (93, 97, stripnulls),
        "comment": (97, 126, stripnulls),
        "genre": (127, 128, ord)
    }

    def __parse(self, filename):
        """parse ID3v1.0 tags from MP3 file"""
        self.clear()
        try:
            fsock = open(filename, 'rb', 0)
            try:
                fsock.seek(-128, 2)  # ???128代表着什么
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":  # 这里在做什么
                for tag, (start, end, parseFunc) in self.tagDataMap.item():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key is "name" and item:
            self.__parse(item)
        super(MP3FileInfo, self).__setitem__()


def listDirectory(directory, fileExtList):
    """get list of file info objects for files of particular extensions"""
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList
                if os.path.splitext(f)[1] in fileExtList]

    def getFileInfoClasses(filename, module=sys.modules[FileInfo.__module__]):
        "get file info classes from filename extension"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module,
                                                     subclass) or FileInfo

    return [getFileInfoClasses(f)(f) for f in fileList]


if __name__ == "__main__":
    for info in listDirectory("/music/_singles/", [".mp3"]):
        print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
        print
