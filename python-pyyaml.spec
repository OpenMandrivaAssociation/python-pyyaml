%define module pyyaml

Summary:	Python package implementing YAML parser and emitter
Name:		python-%{module}
Version:	6.0.3
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pyyaml.org/
# Also https://pypi.org/project/PyYAML/
Source0:	https://files.pythonhosted.org/packages/source/p/pyyaml/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(python)
Provides:	PyYAML = %{EVRD}
%rename python-yaml

%description
PyYAML is a YAML parser and emitter for the Python programming
language.

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%files
%{python_sitearch}/*yaml
%{python_sitearch}/pyyaml-%{version}.dist-info
