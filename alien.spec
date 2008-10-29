%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl.UTF-8):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	8.73
Release:	1
License:	GPL
Group:		Applications/System
#Source0:	http://kitenet.net/programs/alien/%{name}_%{version}.tar.gz
Source0:	http://ftp.de.debian.org/debian/pool/main/a/alien/%{name}_%{version}.tar.gz
# Source0-md5:	9ff7605218ca904e1e21d5f99301c6be
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	44f9b3381776077447bbdb8c64d3f215
Patch0:		%{name}-DESTDIR.patch
URL:		http://kitenet.net/programs/alien/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	/usr/bin/rpm2cpio
Requires:	binutils
Requires:	cpio
Suggests:	/usr/bin/822-date
Suggests:	debhelper
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl.UTF-8
Alien pozwala przekonwertować pakiety Debiana, Stampede oraz Slackware
w pakiety używane w PLD, które mogą być zainstalowane przy użyciu
rpm-a i odwrotnie. Narzędzie to jest przydatne wyłącznie dla pakietów
binarnych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/changelog README TODO
%attr(755,root,root) %{_bindir}/alien
%{_datadir}/alien
%{perl_vendorlib}/Alien
%{_mandir}/man1/alien.1*
%{_mandir}/man3/Alien::Package*.3pm*
%lang(fr) %{_mandir}/fr/man1/alien.1*
%lang(pl) %{_mandir}/pl/man1/alien.1*
