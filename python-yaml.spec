%define real_name PyYAML

Name:           python-yaml
Version:        3.06
Release:        %mkrel 2
Epoch:          0
Summary:        Python package implementing YAML parser and emitter
License:        MIT
Group:          Development/Python
URL:            http://pyyaml.org/
Source0:        http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
Provides:       %{real_name} = %{epoch}:%{version}-%{release}
%py_requires -d
BuildRequires:	yaml-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PyYAML is a YAML parser and emitter for the Python programming
language. 

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%setup -q -n %{real_name}-%{version}

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
%{_bindir}/find %{buildroot} -name \*.egg-info | %{_bindir}/xargs %{__rm}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE README examples
%{python_sitearch}/yaml
%{python_sitearch}/*.so
