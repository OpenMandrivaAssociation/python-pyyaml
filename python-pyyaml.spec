%define _empty_manifest_terminate_build 0
%define module pyyaml

Summary:	Python package implementing YAML parser and emitter
Name:		python-%{module}
Version:	6.0.2
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pyyaml.org/
Source0:	https://files.pythonhosted.org/packages/source/p/pyyaml/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-cython
Provides:	PyYAML = %{EVRD}
Provides:	python3egg(pyyaml)
%rename python-yaml

%description
PyYAML is a YAML parser and emitter for the Python programming
language.

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitearch}/*yaml
%{python_sitearch}/PyYAML-%{version}.dist-info
