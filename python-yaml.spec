%define real_name PyYAML

Name:           python-yaml
Version:        3.09
Release:        %mkrel 7
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0:3.09-4mdv2011.0
+ Revision: 668051
- mass rebuild

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0:3.09-3mdv2011.0
+ Revision: 590784
- rebuild for py2.7

* Wed Dec 02 2009 Funda Wang <fwang@mandriva.org> 0:3.09-2mdv2010.1
+ Revision: 472674
- rebuild for new libyaml

* Wed Dec 02 2009 Funda Wang <fwang@mandriva.org> 0:3.09-1mdv2010.1
+ Revision: 472661
- new version 3.09

* Fri Jan 02 2009 Adam Williamson <awilliamson@mandriva.org> 0:3.08-1mdv2009.1
+ Revision: 323250
- new release 3.08

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 0:3.07-1mdv2009.1
+ Revision: 320837
- New version 3.07

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0:3.06-2mdv2009.1
+ Revision: 318986
- rebuild for new python

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0:3.06-1mdv2009.1
+ Revision: 291764
- New version 3.06

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0:3.05-2mdv2009.0
+ Revision: 225165
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:3.05-1mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 02 2007 David Walluck <walluck@mandriva.org> 0:3.05-1mdv2008.0
+ Revision: 34457
- Import python-yaml



* Fri Jun 01 2007 David Walluck <walluck@mandriva.org> 0:3.05-1mdv2008.0
- release
