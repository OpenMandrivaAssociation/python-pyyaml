%define real_name PyYAML
%define _disable_lto 1
 
Summary:	Python package implementing YAML parser and emitter
Name:		python-yaml
Version:	4.1
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pyyaml.org/
Source0:	https://github.com/yaml/pyyaml/archive/pyyaml-%{version}.tar.gz
BuildRequires:	yaml-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-cython
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources
Provides:	%{real_name} = %{EVRD}
Provides:	python3egg(pyyaml)
 
%description
PyYAML is a YAML parser and emitter for the Python programming
language. 
 
YAML is a data serialization format designed for human readability
and interaction with scripting languages.
 
%package -n python2-yaml
Summary:	Python package implementing YAML parser and emitter
Group:		Development/Python
Requires:	python2
Provides:	pythonegg(pyyaml)
 
%description -n python2-yaml
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

pushd python2
python setup.py build
popd

pushd python3
python setup.py build
popd
 
%install

pushd python2
python setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
popd

pushd python3
python setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
popd

%files -n python-yaml
%doc python2/LICENSE python2/README python2/examples
%{py3_platsitedir}/yaml
%{py3_platsitedir}/*.so
%{py3_platsitedir}/*.egg-info

%files -n python2-yaml
%doc python3/LICENSE python3/README python3/examples
%{py_platsitedir}/yaml
%{py_platsitedir}/*.so
%{py_platsitedir}/*.egg-info
