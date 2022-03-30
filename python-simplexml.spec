%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module  simplexml
Summary:	Simplexml in Python
Summary(pl.UTF-8):	simplexml w Pythonie
Name:		python-%{module}
Version:	0.6.5
Release:	6
License:	GPL
Group:		Libraries/Python
Source0:	http://www.fit.vutbr.cz/~smrcka/projects/simplexml/%{module}-%{version}.tar.gz
# Source0-md5:	a150742499c483a38267a885dca4f245
URL:		http://www.fit.vutbr.cz/~smrcka/projects/simplexml
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
Requires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-2to3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleXML is a commandline tool and library for very simply
manipulating XML files. It lets you harvest data from XML files,
change values of attributes, print or change data of elements, create
new elements, etc. All you need is to know the path to element with
definition of attributes and/or order of element. If you work with
commandline tool, you must also know what do you want (change data,
attributes, create new element, ...) In case you use the python
module, you get an object with attributes like name, attr, value, data
etc.

For help with commandline tool, run it. It's really simple! ;-) For
help with python module, import it and see __doc__ attributes ;-)

Python 2.x version.

%package -n python3-%{module}
Summary:	Simplexml in Python
Summary(pl.UTF-8):	Simplexml w Pythonie
Group:		Libraries/Python

%description -n python3-%{module}
SimpleXML is a commandline tool and library for very simply
manipulating XML files. It lets you harvest data from XML files,
change values of attributes, print or change data of elements, create
new elements, etc. All you need is to know the path to element with
definition of attributes and/or order of element. If you work with
commandline tool, you must also know what do you want (change data,
attributes, create new element, ...) In case you use the python
module, you get an object with attributes like name, attr, value, data
etc.

For help with commandline tool, run it. It's really simple! ;-) For
help with python module, import it and see __doc__ attributes ;-)

Python 2.x version.

%prep
%setup -q -n %{module}-%{version}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' \
      simplexml

%build

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir}/simplexml,%{_bindir}}
install *.py $RPM_BUILD_ROOT%{py_sitescriptdir}/simplexml/
install simplexml $RPM_BUILD_ROOT%{_bindir}
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/simplexml
install *.py $RPM_BUILD_ROOT%{py3_sitescriptdir}/simplexml/
%endif

%if %{with python2}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
2to3 -w -n $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/simplexml
%dir %{py_sitescriptdir}/simplexml
%{py_sitescriptdir}/simplexml/*
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/simplexml
%{py3_sitescriptdir}/simplexml/*
%endif
