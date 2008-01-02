%define real_name PyYAML

Name:           python-yaml
Version:        3.05
Release:        %mkrel 1
Epoch:          0
Summary:        Python package implementing YAML parser and emitter
License:        GPL
Group:          Development/Python
URL:            http://pyyaml.org/
Source0:        http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
Provides:       %{real_name} = %{epoch}:%{name}-%{version}
%py_requires -d
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PyYAML is a YAML parser and emitter for the Python programming
language. 

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O2 --skip-build --root=%{buildroot} --prefix=%{_prefix}
%{_bindir}/find %{buildroot} -name \*.egg-info | %{_bindir}/xargs %{__rm}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README examples
%defattr(-,root,root,0755)
%{py_puresitedir}/yaml
