%define _empty_manifest_terminate_build 0
%define real_name PyYAML
%define module pyyaml

Summary:	Python package implementing YAML parser and emitter
Name:		python-%{module}
Version:	6.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://pyyaml.org/
Source0:	https://files.pythonhosted.org/packages/36/2b/61d51a2c4f25ef062ae3f74576b01638bebad5e045f747ff12643df63844/%{real_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-cython
Provides:	%{real_name} = %{EVRD}
Provides:	python3egg(pyyaml)
%rename python-yaml

%description
PyYAML is a YAML parser and emitter for the Python programming
language.

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%autosetup -p1 -n %{real_name}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitearch}/*yaml
%{python_sitearch}/*.egg-info
