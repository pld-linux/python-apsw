
%define		module	apsw

Summary:	Another Python SQLite Wrapper
Summary(pl):	Another Python SQLite Wrapper - jeszcze jeden pythonowy wrapper dla SQLite
Name:		python-%{module}
Version:	3.2.2
Release:	1
License:	Free
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/bitpim/%{module}-%{version}-r1.zip
# Source0-md5:	f18221ecb428036a33efb2ac0294f85e
URL:		http://www.rogerbinns.com/apsw.html
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APSW provides an SQLite 3 wrapper that provides the thinnest layer
over SQLite 3 possible. Everything you can do from the C API to SQLite
3, you can do from Python. Although APSW looks vaguely similar to the
DBAPI, it is not compliant with that API and instead works the way
SQLite 3 does.

%description -l pl
APSW udost�pnia wrapper SQLite 3 dostarczaj�cy najcie�sz� jak to tylko
mo�liwe warstw� ponad SQLite 3. Wszystko co mo�na zrobi� z poziomu API
C SQLite 3 mo�na zrobi� tak�e z poziomu Pythona. Chocia� APSQ wygl�da
dosy� podobnie do DBAPI, nie jest kompatybilne z tym API, natomiast
dzia�a tak, jak SQLite 3.

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
%doc *.html
%attr(755,root,root) %{py_sitedir}/%{module}.so
