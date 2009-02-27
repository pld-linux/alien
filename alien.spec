%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl.UTF-8):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	8.74
Release:	1
License:	GPL
Group:		Applications/System
#Source0:	http://kitenet.net/programs/alien/%{name}_%{version}.tar.gz
Source0:	http://ftp.de.debian.org/debian/pool/main/a/alien/%{name}_%{version}.tar.gz
# Source0-md5:	3f049384e39e3ab79b6b298068f38f77
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	44f9b3381776077447bbdb8c64d3f215
URL:		http://kitenet.net/~joey/code/alien/
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
%setup -q -n %{name} -c -T

exit 1

%build

%install

%clean

%files
