Summary:	A PHP source editor for GNOME 2.
Summary(pl):	Edytor kodu php dla GNOME 2.
Name:		gphpedit
Version:	0.4.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gphpedit.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	513caedaff7dac8a697d520c64f56e86
URL:		http://www.gphpedit.org/
BuildRequires:	GtkScintilla2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gPHPEdit is a GNOME2 editor dedicated to editing PHP files and other
supporting files like HTML/CSS.

%description -l pl
gPHPEdit jest edytorem dla srodowiska GNOME2 przeznaczonym do edycji 
plikow PHP i innych wspieranych formatow jak HTML/CSS.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
./configure

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README

%attr(755,root,root) %{_bindir}/gphpedit
%{_datadir}/pixmaps/gphpedit.png
%{_datadir}/applications/gphpedit.desktop
%{_datadir}/gphpedit/php-gphpedit.api
