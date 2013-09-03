
%define		module	apsw

Summary:	Another Python SQLite Wrapper
Summary(pl.UTF-8):	Another Python SQLite Wrapper - jeszcze jeden pythonowy wrapper dla SQLite
Name:		python-%{module}
Version:	3.8.0.1
Release:	1
License:	Free
Group:		Development/Languages/Python
Source0:	http://apsw.googlecode.com/files/%{module}-%{version}-r1.zip
# Source0-md5:	2ea61c66ce40cbe3d10ea16c633867de
URL:		http://code.google.com/p/apsw/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= 3.8.0
BuildRequires:	unzip
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

%prep
%setup -q -n %{module}-%{version}-r1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/%{module}-*.egg-info
