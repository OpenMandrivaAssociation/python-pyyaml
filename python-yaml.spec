%define real_name PyYAML
 
Summary:	Python package implementing YAML parser and emitter
Name:		python-yaml
Version:	3.10
Release:	7
License:	MIT
Group:		Development/Python
Url:		http://pyyaml.org/
Source0:	http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
BuildRequires:	yaml-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
Provides:	%{real_name} = %{EVRD}
 
%description
PyYAML is a YAML parser and emitter for the Python programming
language. 
 
YAML is a data serialization format designed for human readability
and interaction with scripting languages.
 
%package -n python3-yaml
Summary:	Python package implementing YAML parser and emitter
Group:		Development/Python
Requires:	python3
 
%description -n python3-yaml
PyYAML is a YAML parser and emitter for the Python programming
language. 
 
YAML is a data serialization format designed for human readability
and interaction with scripting languages.
 
%prep
%setup -q -c

mv %{real_name}-%{version} python2
cp -r python2 python3
 
%build
export CFLAGS="%{optflags}"

pushd python2
%{__python} setup.py build
popd

pushd python3
%{__python3} setup.py build
popd
 
%install

pushd python2
%{__python} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
popd

pushd python3
%{__python3} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
popd

%files -n python-yaml
%doc python2/LICENSE python2/README python2/examples
%{python_sitearch}/yaml
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info

%files -n python3-yaml
%doc python3/LICENSE python3/README python3/examples
%{python3_sitearch}/yaml
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info

