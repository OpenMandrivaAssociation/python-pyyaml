%define real_name PyYAML
%define _disable_lto 1
%define module pyyaml

Summary:	Python package implementing YAML parser and emitter
Name:		python-%{module}
Version:	6.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pyyaml.org/
Source0:	https://files.pythonhosted.org/packages/36/2b/61d51a2c4f25ef062ae3f74576b01638bebad5e045f747ff12643df63844/PyYAML-6.0.tar.gz
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
%setup -qn PyYAML-%{version}
%build
export CFLAGS="%{optflags} -fno-lto"

pushd yaml
rm -fv _yaml.c
popd
%py_build

%install
%py_install

%files -n python-%{module}
%{python_sitearch}/*yaml
%{python_sitearch}/*.egg-info
