%define real_name PyYAML

Name:           python-yaml
Version:        3.10
Release:        %mkrel 1
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
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --skip-build --root=%{buildroot} --record=FILE_LIST

%clean
%{__rm} -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,0755)
%doc CHANGES LICENSE README examples/
