======
metaindex
======
---------------------------
document search by metadata
---------------------------

Synopsis
========

::

  metaindex [-h] [-l loglevel] [-c configuration file] {add,find,index,remove,fs}


Description
===========

With metaindex you can find files on your disk based on their metadata, like
the title of a PDF, the keywords of an ebook, or the model of a camera that
a photo was taken with.

The following types of files are supported:

 - Images (anything that has EXIF, IPTC, or XMP information),
 - Audio (audio file formats that have ID3 header or similar),
 - Video (most video file formats have an ID3 header),
 - PDF,
 - ebooks (epub natively, calibre metadata files are understood, too).

User provided extra metadata is supported, if it’s provided in the same
directory as the file and the metadata file is ``.metadata.json``. See
`Extra Metadata`_ below for more details.


Options
=======

General parameters are:

  ``-c configuration file``
    Use this configuration file instead of the one from the default
    location.

  ``-h``
    Show the help.

  ``-l loglevel``
    Set the level of details shown in logging. Your options are ``fatal``,
    ``error``, ``warning``, ``info``, and ``debug``. Defaults to ``warning``.

metaindex operates in one of the modes ``add``, ``index``, ``find`` or
``remove``. If you want to try the experimental filesystem mode, there is
also ``fs``.


Add
---

``Add`` allows you to add extra metadata to the given files::

  metaindex add [-a] [-r] [-u] [-t tags] [--] [paths]

The extra metadat will be added to the existing metadata sidecar file in
the same directory that each file is located in. If no metadata sidecar
file exists yet, it will be created.

The options to this command are

  ``-t tags``
    Tags to set. Have to be provided in the form of ``tag:value``. If you
    want to set multiple tags, give one after the other, like this::

      metaindex add -t "title:The Albatross" author:Gumby -- paper1.pdf

  ``-a``
    Apply changes only all files (and future files) of a directory.
    If one of the paths is a directory this option will make sure that a
    ``*`` entry is added to the ``.metadata.json`` file, effectively adding
    the new tags to all current and all future files of this directory.

  ``-r``
    Add the tags to all files in all subdirectories, too.
    In combination with the ``-a`` option the new tags will be applied to
    all subdirectories (and their subdirectories, and so on) for all paths
    that are pointing to directories (creating a ``**`` entry).

  ``-u``
    Update the cache after adding all metadata. If you do not provide this
    parameter, the cache will not receive the newly made changes and the
    next search will not automatically show these added tags.

  ``paths``
    The paths to files or directories to add the tags to.
    If a path is pointing to a directory, the metadata will be applied to
    all files in the directory separately (creating an entry for each file
    of the directory in the metadata sidecar file).


Find
----

This is the main operation used to search for files::

  metaindex find [-l directory] [-f [-k]] [-t [tags]] [--] [search queries]

The options to this command are

  ``-t [tags]``
    Metadata tags that you wish to see per found file.

  ``-l directory``
    If this option is provided, metaindex will create this directory (or use
    the existing directory only if it is empty) and create a symbolic link
    to all files that matches this search.

  ``-f``
    Enforce the use of ``-l``’s ``directory``, even if it is not empty.
    Still, metaindex will only work with that directory if it contains only
    symbolic links (e.g. a previous search result)!
    If ``-f`` is provided, all symbolic links in ``directory`` will be
    deleted and the links of this search will be put in place.

  ``-k``
    When you use ``-l`` and ``-f``, ``-k`` will keep all existing links in
    the search directory. That means you can accumulate search results in
    one directory.

  ``search queries``
    The terms to search for. If left empty, all files will be found. See
    below in section `Search Query Syntax`_ for the details on search
    queries.
    If the search query is only given as ``-``, metaindex will read the search
    query from stdin.


Index
-----

This is the operation to index files and store that information in the
cache::

  metaindex index [-C] [-r] [-p processes] [-i [paths]]

The options to this command are

  ``-C``
    Clear the cache. If combined with other options, the flushing of the
    cache will happen first.

  ``-m``
    Remove missing files. When a file, that's in the index, can not be
    found on disk anymore, it will be removed when this option is enabled.
    By default this option is disabled.

  ``-i [paths]``
    Run the indexer on these paths. If no paths are provided, all paths in
    the cache are revisited and checked for changes.
    If ``paths`` is ``-``, the list of files will be read from stdin, one
    file per line.

  ``-p processes``
    By default metaindex will run as many indexer processes in parallel as
    CPUs are available on the computer. This parameter allows you to define
    how many indexers may be run at the same time.

  ``-r``
    Run the indexer recursively. That means to visit all files in all
    subdirectories of the paths in the ``-i`` parameter.


Remove
------

This operation can be used to remove metadata from files and
(sub)directories::

  metaindex remove [-t tags] [-x] [-u] [-r] [--] [paths]

With this option it is possible to soft-remove metadata tags of files
without editing them directly. For example, if one of your epubs has an
inconvenient title in the metadata, you could run ``metaindex remove -t
opf.title -- that-book.epub``. It would not edit the epub, but add a field
in the sidecar file to not add the epub’s title into the cache.

The options for this command are:

  ``-t tags``
    The tags to remove by name (case-sensitive). Can be a synonym (see
    `Synonyms`_ below). To remove several tags in the same command, just
    add them after the ``-t``, like this::

      metaindex remove -t opf.title opf.subject opf.summary -- that-book.epub

  ``-x``
    Just remove all extra metadata that was provided in the user defined
    sidecar files.

  ``-u``
    Update cache after removing the tags. If you do not provide this
    option, the cache will be outdated and you can still find the removed
    tags.

  ``-r``
    Remove tags recursively. That means the tags will also be removed from
    all subdirectories (if you provide any directories in ``paths``).

  ``paths``
    The paths to the files and/or directories for which you want to remove
    the given metadata tags.
    If you provide a directory in the paths, the given tags will be removed
    from all files in that directory.


Filesystem (fs)
---------------

On Linux you can try the experimental feature of mounting a FuseFS that
will give you a structured access to your files through their metadata::

  metaindex fs [command] [mount point]

The only supported command so far is ``mount``.

It is very experimental and not very useful, but at the same time will not
break any of your files as it only provides a read-only view on your tagged
files.


Files
=====

metaindex is controlled through a configuration file and caches metadata in a
cache file.


Cache file
----------

The cache file is usually located in ``~/.cache/metaindex/index.db``, but that
location is configurable.


Configuration file
------------------

The configuration file is usually located in ``~/.config/metaindex.conf``. An
example of the configuration file is provided in the ``dist`` directory.
The syntax of the file is::

  [Category]
  option = value

There are several categories in the configuration file, the possible
options are described after this list:

 - ``[General]``, general options
 - ``[Synonyms]``, synonyms for tag names
 - ``[Include]``, additional configuration files that have to be included


General
~~~~~~~

  ``cache``
    The location of the cache file. Defaults to
    ``~/.cache/metaindex/index.db``.

  ``recursive-extra-metadata``
    When looking for sidecar metadata files (see `Extra Metadata`_), also
    look in all parent directories for metadata. Defaults to ``yes``.

    This is useful when the file is ``collection/part/file.jpg`` but the
    metadata file is ``collection/.metadata.json`` (and in this metadata
    file the reference is made to ``part/file.jpg``).

  ``collection-metadata``
    Some sidecar files can define metadata that applies to the entire
    collection of files in that directory. This options controls what
    files may define that type of metadata.
    Based on the available metadata storage modules (e.g. JSON, and OPF)
    these names are extended by the corresponding file extensions.
    Defaults to ``.metadata, metadata``.

    That means, with JSON and OPF enabled, that the metadata files
    ``.metadata.json, .metadata.opf, metadata.json, metadata.opf`` are
    considered.

    See below in `Extra Metadata`_ for more details.

  ``ignore-dirs``
    What folders (and their subfolders) to ignore entirely. One folder per
    line. Defaults to ``.git`` and ``System Volume Information``.

  ``ignore-tags``
    What (automatically extracted) tags to not add to the cache and thus
    prevent them being searchable. Comma-separated list of the tags.
    Defaults to: ``Exif.Image.StripByteCounts, Exif.Image.StripOffsets``.

  ``mimetypes``
    If you have additional mimetypes that you would like metaindex to know,
    this is the option you can use to point to additional mimetype files.
    To add multiple files, separate them by a newline. No matter what files
    you provide here, you system's mimetype file will always be used.


Synonyms
~~~~~~~~

Some metadata fields have less convenient names than others, but might
semantically be the same. For example, ``Xmp.xmp.CreatorTool`` and
``pdf.Creator`` both mean "The program that was used to create this file".

For convenience it is possible to define synonyms, so you only have to
search for ``author`` when you mean to search for ``id3.artist``,
``pdf.Author``, or ``Exif.Image.Artist``.

The section ``[Synonyms]`` in the configuration file is the place to define
these synonyms. Here are the defaults, that you don’t have to set up::

  [Synonyms]
  author = extra.author, extra.artist, id3.artist, pdf.Author, Exif.Image.Artist
  title = extra.title, id3.title, pdf.Title, Xmp.dc.title, extra.opf.title
  tags = extra.tags, pdf.Keywords, pdf.Categories, Xmp.dc.subject, extra.subject, pdf.Subject, opf.subject, extra.opf.subject
  language = opf.language, pdf.Language, Xmp.dc.language, extra.language, extra.opf.language
  series = extra.series
  series_index = extra.series_index


Include
~~~~~~~

You can include additional configuration files (for example to split up
your configuration into multiple files).

All the ``name = path`` entries in the ``[Include]`` section will be loaded
in the alphabetical order of the names.

In this example ``~/.metaindex.conf`` will be loaded and then
``/tmp/metaindex.conf``. Both of course only after the main configuration file::

  [Include]
  xtra = /tmp/metaindex.conf
  extra = ~/.metaindex.conf

Additional ``[Includes]`` in these included configuration files are ignored
though.


Search Query Syntax
===================

If the search term only contains a simple word, like ``albatross``, all
files will be found that contain this word in any metadata field.

To search for a phrase containing spaces, you have to enclose the phrase in
blockquotes or single quotes, like ``"albatross flavour"``.

To search for "albatross" in a specific metadata field, like in the title,
you have to search for ``title:albatross``. Again, the phrase search
requires quotes: ``title:"albatross flavour"``.

You can search files by the existance of a metadata tag by adding a ``?``
after the name of the metadata tag. For example, to find all files that
have the ``resolution`` metadata tag: ``resolution?``.

When the search includes the tag name, you have to provide the full
case-sensitive name of the tag. ``artist`` and ``Artist`` are very
different tag names and just searching for ``artist:tim`` when you mean to
search for ``albumartist`` will not result in the same search results.

Have a look at the `Synonyms`_ feature to find out how to search
conveniently for more complex tag names.

When searching for multiple terms, you can choose to connect the terms with
``and`` or ``or``. ``and`` is the default if none is provided, so these two
search queries, to find all photos made with a Canon camera and with a
width of 1024 pixels, are the same::

  resolution:1024x Exif.Image.Model:canon

  resolution:1024x and Exif.Image.Model:canon

To search for all pictures that are made with a Canon camera or have that
width, you have to use ``or``::

  resolution:1024x or Exif.Image.Model:canon


Metadata tags
-------------

These metadata tags are always available:

  ``last_accessed``
    A timestamp when the file was accessed the last time (if the OS
    supports it).

  ``last_modified``
    A timestamp when the file was modified the last time (if the OS
    supports it).

  ``filename``
    The name of the file on disk including extensions.

  ``size``
    The file size in bytes.

  ``mimetype``
    The mimetype of the file, if it could be detected.


Extra Metadata
==============

Not all filetypes support metadata (plain text files, for example) and
using extra files on the side (but in the same directory as the file to be
tagged) is used. These files on the side are called "sidecar files".

Sidecar files are expected to have the same filename as the file that they
are describing, but with a different extension, based on how the
description is provided. So, if you want to add additional metadata to your
``moose.jpg``, you could create a ``moose.json`` sidecar file or a
``moose.opf`` file.

All metadata provided by extra sidecar files is cached with the ``extra.``
prefix. For example, if your metadata file tags a file with ``title``, you
can search for it by looking for ``extra.title``.

metaindex supports sidecar files in JSON format like this when the file is
used for several files::

  {
   "file.ext": {
    "title": "An example file",
    "authors": ["dr Gumby", "The Bishop"],
    "Xmp.dc.title": null
   }
  }

Or like this if the JSON file is used for only one file::

  {
    "title": "A long story",
    "date": 2012-05-01
  }

The special value of ``null`` allows you to ignore a metadata tag from that
file, i.e. if that file has the ``Xmp.dc.title`` tag, it will be ignored.

Calibre style sidecar files, usually called ``metadata.opf`` are also
supported.


Collection Metadata
-------------------

Sometimes all files in a directory should receive the same set of metadata.
This is called "Collection metadata" and can be accomplished in JSON
sidecar files (like ``.metadata.json``) by adding an entry ``"*"``, like
this::

  {
    "*": {
      "tags": ["tag1", "tag2"]
    },
    "file.tif": {
      "tags": ["tag3"]
    }
  }

Suppose you have this ``.metadata.json`` in a directory with two files,
``file.tif`` and ``other.csv``. Both files will receive the tags ``tag1``
and ``tag2``, but only ``file.tif`` will have all three tags.

For collection metadata to work properly, the `General`_ option
``collection-metadata`` must be set to the names of sidecar files that are
allowed to define collection metadata.

By default files like ``.metadata.json``, and ``metadata.opf``
are expected to contain extra metadata (see `General`_ options above).
If your metadata files are called
differently, for example ``meta.json`` and ``.extra.json``, you can
configure that in the metaindex configuration file::

  [General]
  collection-metadata = meta, .extra

The filenames listed in ``collection-metadata`` will be excluded from indexing,
so they will not show up when you search for them (e.g. via ``metaindex find
filename:metadata``)!


Recursive Collection Metadata
-----------------------------

If you want to apply the collection metadata not only to the files of the
sidecar’s directory, but also in all subdirectories, you can use the
"recursive collection metadata" ``"**"``.

This is useful if you already have your data structured in directories, for
example in this way: ``pictures/nature/animals/duck.jpg``.

Here you could add a ``.metadata.json`` file in the ``nature`` directory
with this recursive directive::

  {
    "**": {
      "tags": ["nature"]
    }
  }

Now not only the files in ``nature`` are tagged as ``nature``, but also
all files in ``animals``.

You can disable this functionality entirely by setting the `General`_
option ``recursive-collection-metadata`` to an empty string::

  [General]
  recursive-collection-metadata =

**Caveat**: you can not defined both, a recursive and a non-recursive set
of collection metadata in the same directory::

  {
    "*": {
      "description": "BROKEN EXAMPLE: this does not work!"
    },
    "**": {
      "title": "BROKEN EXAMPLE! 'title' AND 'description' will be applied to all
      subdirectories!"
    }
  }


Usage Examples
==============

Index some directories
----------------------

To index you ``Documents`` and ``Pictures`` folder recursively::

  metaindex index -r -i ~/Documents ~/Pictures


Reindex all files
-----------------

To only update the metadata from all known files::

  metaindex index -i


Find all files
--------------

List all files that are in cache::

  metaindex find


Find file by mimetype
---------------------

Searching for all ``image/*`` mimetypes can be accomplished by this::

  metaindex find mimetype:^image/


Listing metadata
----------------

To list all metadata tags and values of all odt files::

  metaindex find -t -- "filename:odt$"

List the resolutions of all files that have the ``resolution`` metadata tag::

  metaindex find -t resolution -- "resolution?"


Bugs
====

Surely. Please report anything that you find at
https://github.com/vonshednob/metaindex or via email to the authors.

