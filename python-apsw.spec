#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	apsw
%define		sqlite_ver 3.8.5

Summary:	Another Python SQLite Wrapper
Summary(pl.UTF-8):	Another Python SQLite Wrapper - jeszcze jeden pythonowy wrapper dla SQLite
Name:		python-%{module}
Version:	3.8.5
Release:	12
License:	Free
Group:		Libraries/Python
Source0:	https://github.com/rogerbinns/apsw/archive/%{version}-r1.tar.gz
# Source0-md5:	09eb9f39d7cf9d320ee8e89f9e9ab7ea
URL:		http://rogerbinns.github.io/apsw/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= %{sqlite_ver}
BuildRequires:	unzip
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
Requires:	sqlite3 >= %{sqlite_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APSW provides an SQLite 3 wrapper that provides the thinnest layer
over SQLite 3 possible. Everything you can do from the C API to SQLite
3, you can do from Python. Although APSW looks vaguely similar to the
DBAPI, it is not compliant with that API and instead works the way
SQLite 3 does.

%description -l pl.UTF-8
APSW udostępnia wrapper SQLite 3 dostarczający najcieńszą jak to tylko
możliwe warstwę ponad SQLite 3. Wszystko co można zrobić z poziomu API
C SQLite 3 można zrobić także z poziomu Pythona. Chociaż APSQ wygląda
dosyć podobnie do DBAPI, nie jest kompatybilne z tym API, natomiast
działa tak, jak SQLite 3.

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	sqlite3 >= %{sqlite_ver}

%description -n python3-%{module}
APSW provides an SQLite 3 wrapper that provides the thinnest layer
over SQLite 3 possible. Everything you can do from the C API to SQLite
3, you can do from Python. Although APSW looks vaguely similar to the
DBAPI, it is not compliant with that API and instead works the way
SQLite 3 does.

%description -n python3-%{module} -l pl.UTF-8
APSW udostępnia wrapper SQLite 3 dostarczający najcieńszą jak to tylko
możliwe warstwę ponad SQLite 3. Wszystko co można zrobić z poziomu API
C SQLite 3 można zrobić także z poziomu Pythona. Chociaż APSQ wygląda
dosyć podobnie do DBAPI, nie jest kompatybilne z tym API, natomiast
działa tak, jak SQLite 3.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}-r1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitedir}/%{module}*.so
%{py3_sitedir}/%{module}-%{version}*-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
