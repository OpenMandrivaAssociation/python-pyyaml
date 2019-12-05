%define real_name PyYAML
%define _disable_lto 1
%define module pyyaml
 
Summary:	Python package implementing YAML parser and emitter
Name:		python-%{module}
Version:	5.2
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pyyaml.org/
Source0:	https://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-cython
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources
Provides:	%{real_name} = %{EVRD}
Provides:	python3egg(pyyaml)
Provides:	python-yaml = %{EVRD}
 
%description
PyYAML is a YAML parser and emitter for the Python programming
language. 
 
YAML is a data serialization format designed for human readability
and interaction with scripting languages.
 
%package -n python2-%{module}
Summary:	Python package implementing YAML parser and emitter
Group:		Development/Python
Requires:	python2
Provides:	pythonegg(pyyaml)
Provides:	python2-yaml = %{EVRD}
 
%description -n python2-%{module}
PyYAML is a YAML parser and emitter for the Python programming
language. 
 
YAML is a data serialization format designed for human readability
and interaction with scripting languages.
 
%prep
%setup -q -c

mv %{real_name}-%{version} python2
cp -r python2 python3

# Rebuild the Cython-generated code, only cython >= 0.27.3 supporty Python 3.7
cd python3/ext
cython _yaml.pyx
 
%build
export CFLAGS="%{optflags} -fno-lto"

cd python2
%{__python2} setup.py build
cd -

cd python3
%{__python} setup.py build
cd -
 
%install

cd python2
%{__python2} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
cd -

cd python3
%{__python} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
cd -

%files -n python-%{module}
%doc python2/LICENSE python2/README python2/examples
%{python3_sitearch}/yaml
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info

%files -n python2-%{module}
%doc python3/LICENSE python3/README python3/examples
%{python2_sitearch}/yaml
%{python2_sitearch}/*.so
%{python2_sitearch}/*.egg-info

