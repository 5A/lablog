# Backend Data

This directory contains files that are used as storage for backend of lablog.

As stated in the lablog architecture, no relational database is used for lablog, and everything is exchanged, stored as simple text files. This makes it easy for lablog to be deployed across the cloud and distributionally.

## Files

`blogdata.json` contains two sections: `posts` and `comments`:

- `posts` contains metadata about posts, including post titles, abstracts, created times, sorting ranks, etc.

- `comments` contains data and metadata about comments, including commenter's name, address, content, etc.
