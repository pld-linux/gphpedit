Summary:	A PHP source editor for GNOME 2
Summary(pl):	Edytor kodu php dla GNOME 2
Name:		gphpedit
Version:	0.4.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gphpedit.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	513caedaff7dac8a697d520c64f56e86
URL:		http://www.gphpedit.org/
BuildRequires:	GtkScintilla2-devel
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gPHPEdit is a GNOME2 editor dedicated to editing PHP files and other
supporting files like HTML/CSS.

%description -l pl
gPHPEdit jest edytorem dla ¶rodowiska GNOME2 przeznaczonym do edycji
plików PHP i innych wspieranych formatów jak HTML/CSS.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gphpedit
%{_pixmapsdir}/gphpedit.png
%{_desktopdir}/gphpedit.desktop
%{_datadir}/gphpedit
