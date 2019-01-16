---
layout:     post
title:     SQLAlchemy Siêu Cơ Bản
date:      2019-01-16 17:11:46.835175
summary:   
permalink:	sqlalchemy-sieu-co-ban
tags: 
---

The SQLAlchemy SQL Toolkit and Object Relational Mapper a comprehensive set of tools for working with
databases and Python. It has several distinct areas of which can be used individually or combined
together. Its major components are illustrated below, component dependencies organized into layers:

![](https://docs.sqlalchemy.org/en/latest/_images/sqla_arch_small.png)



## Documentation Overview

The documentation is separated into three sections: [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/orm/index.html), [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/index.html), and [Dialects](https://docs.sqlalchemy.org/en/latest/dialects/index.html).

In [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/orm/index.html), the Object Relational Mapper is introduced and fully described. New users should begin with the [Object Relational Tutorial](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html). If you want to work with higher-level SQL which is constructed automatically for you, as well as management of Python objects, proceed to this tutorial.



In [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/index.html), the breadth of SQLAlchemy’s SQL and database and description services are documented, the core of which is the Expression language. The SQL Expression Language is a toolkit all its own, of the ORM package, which can be used to construct manipulable SQL which can be programmatically constructed, modified, and executed, cursor-like result sets. In contrast to the ORM’s domain-centric
mode of usage, the expression language provides a schema-centric usage . New users should begin here with [SQL Expression Language Tutorial](https://docs.sqlalchemy.org/en/latest/core/tutorial.html).

































