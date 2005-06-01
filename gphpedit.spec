Summary:	A PHP source editor for GNOME 2
Summary(pl):	Edytor kodu PHP dla GNOME 2
Name:		gphpedit
Version:	0.9.50
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.gphpedit.org/download/files/%{name}-%{version}.tar.gz
# Source0-md5:	5683f1f196d8c80bdad587a043423046
Patch0:		%{name}-desktop.patch
URL:		http://www.gphpedit.org/
BuildRequires:	GtkScintilla2-devel
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gPHPEdit is a GNOME2 editor dedicated to editing PHP files and other
supporting files like HTML/CSS.

%description -l pl
gPHPEdit jest edytorem dla ¶rodowiska GNOME2 przeznaczonym do edycji
plików PHP i innych wspieranych formatów jak HTML/CSS.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
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
