Name:		ncc
Summary:	C source code analyzer
Version:	2.8
Release:	4
License:	Artistic
Group:		Development/Other
URL:		http://students.ceid.upatras.gr/~sxanth/ncc
Source0:	%{name}-%{version}.tar.gz
Patch0:		ncc-2.8-nognu-location.patch
BuildRequires:	pkgconfig(ncurses)

%description
ncc is a compiler that produces program analysis information.

ncc is a decent replacement of cflow and cscope able to analyse any program
using the gcc compiler. The program also includes a graphical call-graph
navigator and source browser which is extremely practical for hacking and
comprehending large projects.

%prep
%setup -q

%patch0 -p1

perl -pi -e "s|ln (.*) ..BINDIR..(.*) ..BINDIR./(.*)|ln \$1 %{_bindir}/\$2 %{buildroot}%{_bindir}/\$3|g;" Makefile
perl -pi -e "s|cp doc/nognu|#|g;" Makefile

%build
%make

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%makeinstall DESTDIR=%{buildroot}%{_prefix}

%files
%doc doc/*
%doc %{_mandir}/man?/ncc*
%{_bindir}/ncc
%{_bindir}/nccar
%{_bindir}/nccc++
%{_bindir}/nccg++
%{_bindir}/nccld
%{_bindir}/nccnav
%{_bindir}/nccnavi
%{_bindir}/nccstrip2.py

