Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	6.44
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://kitenet.net/programs/alien/%{name}.tar.gz
URL:		http://kitenet.net/programs/code/alien/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Joey Hess <joey@kitenet.net>
Buildarch:	noarch

%description
Alien allows you to convert Debian, Stampede and Slackware Packages into
PLD packages, which can be installed with rpm. It can also convert into
Slackware, Debian, and Stampede packages. This is a tool only suitable for
binary packages.

%description -l pl
Alien pozwala Ci przekonwertowaæ pakiety Debiana, Stampede oraz Slackware w
pakiety u¿ywane w PLD, które mog± byæ zainstalowane przy u¿yciu rpm'a i
odwrotnie. Narzêdzie to jest przydatne wy³±cznie dla pakietów binarnych.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

umask 022
make DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_bindir}/alien
%attr(-,root,root) %{_datadir}/alien
%{_mandir}/man*/*
