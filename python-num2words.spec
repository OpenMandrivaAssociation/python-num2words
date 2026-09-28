Name:		python-num2words
Version:	0.5.14
Release:	1
Summary:	Modules to convert numbers to words. Easily extensible
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://pypi.org/project/num2words/
Source0:	num2words-0.5.14.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(docopt)
BuildArch:	noarch
%description
Modules to convert numbers to words. Easily extensible.

%files
%{py_sitedir}/*
%{_bindir}/num2words
