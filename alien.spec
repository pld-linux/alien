Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl):	Konwerter pakiet�w (tgz, rpm, deb, slp)
Name:		alien
Version:	7.5
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	http://kitenet.net/programs/code/alien/%{name}_%{version}.tar.gz
Patch0:	alien-DESTDIR.patch
URL:		http://kitenet.net/programs/code/alien/
BuildRequires: perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Joey Hess <joey@kitenet.net>
Buildarch:	noarch

%include /usr/lib/rpm/macros.perl

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl
Alien pozwala Ci przekonwertowa� pakiety Debiana, Stampede oraz
Slackware w pakiety u�ywane w PLD, kt�re mog� by� zainstalowane przy
u�yciu rpm'a i odwrotnie. Narz�dzie to jest przydatne wy��cznie dla
pakiet�w binarnych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{perl_sitearch},%{perl_sitelib}}
%{__make} DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/alien
%{_datadir}/alien
%{perl_sitelib}/Alien
%{perl_sitearch}
%{_mandir}/man*/*
