%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	7.24
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://kitenet.net/programs/code/alien/%{name}_%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-DESTDIR.patch
URL:		http://kitenet.net/programs/code/alien/
Vendor:		Joey Hess <joey@kitenet.net>
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl
Alien pozwala Ci przekonwertowaæ pakiety Debiana, Stampede oraz
Slackware w pakiety u¿ywane w PLD, które mog± byæ zainstalowane przy
u¿yciu rpm'a i odwrotnie. Narzêdzie to jest przydatne wy³±cznie dla
pakietów binarnych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{perl_archlib},%{perl_sitelib},%{perl_sitearch}} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3}
	
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install blib/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install blib/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/alien
%{_datadir}/alien
%{perl_sitelib}/Alien
%{_mandir}/man*/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*
