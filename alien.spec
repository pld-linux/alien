%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl):	Konwerter pakiet�w (tgz, rpm, deb, slp)
Name:		alien
Version:	8.43
Release:	1
License:	GPL
Vendor:		Joey Hess <joey@kitenet.net>
Group:		Applications/System
Source0:	http://kitenet.net/programs/alien/%{name}_%{version}.tar.gz
# Source0-md5:	c4d8c439e1a403d2138553f735f66143
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	44f9b3381776077447bbdb8c64d3f215
Patch0:		%{name}-DESTDIR.patch
URL:		http://kitenet.net/programs/alien/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	cpio
Requires:	%{_bindir}/rpm2cpio
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl
Alien pozwala przekonwertowa� pakiety Debiana, Stampede oraz
Slackware w pakiety u�ywane w PLD, kt�re mog� by� zainstalowane przy
u�yciu rpm-a i odwrotnie. Narz�dzie to jest przydatne wy��cznie dla
pakiet�w binarnych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/alien
%{_datadir}/alien
%{perl_vendorlib}/Alien
%{_mandir}/man*/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*