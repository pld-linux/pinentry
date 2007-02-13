#
# Conditional build:
%bcond_without	gtk	# without GTK+ 1.x dialog
%bcond_without	gtk2	# without GTK+ 2 dialog
%bcond_without	qt	# without Qt dialog
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl.UTF-8):	Proste kontrolki dialogowe do wpisywania PIN-ów lub haseł
Name:		pinentry
%define		_snap		20061028
Version:	0.7.2
Release:	1.%{_snap}
License:	GPL
Group:		Applications
#Source0:	ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	f30d6d3790add93d2a49390512c3ea56
Patch0:		%{name}-system-assuan.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7.6
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.4.0}
BuildRequires:	libassuan-devel >= 1:0.6.0
BuildRequires:	libcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel}
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details. Base package contains
curses-based dialog.

%description -l pl.UTF-8
Jest to zestaw prostych kontrolek dialogowych do wpisywania PIN-ów lub
haseł, używające protokołu Assuan opisanego w projekcie aegypten;
więcej szczegółów pod adresem http://www.gnupg.org/aegypten/.
Podstawowy pakiet zawiera kontrolkę opartą na curses.

%package gtk
Summary:	Simple PIN or passphrase entry dialog for GTK+ 1.x
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 1.x
Group:		X11/Applications

%description gtk
Simple PIN or passphrase entry dialog for GTK+ 1.x.

%description gtk -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 1.x.

%package gtk2
Summary:	Simple PIN or passphrase entry dialog for GTK+ 2
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2
Group:		X11/Applications
Requires:	gtk+2 >= 2:2.4.0

%description gtk2
Simple PIN or passphrase entry dialog for GTK+ 2.

%description gtk2 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2.

%package qt
Summary:	Simple PIN or passphrase entry dialog for Qt
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt
Group:		X11/Applications

%description qt
Simple PIN or passphrase entry dialog for Qt.

%description qt -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--enable-maintainer-mode \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--%{!?with_gtk:dis}%{?with_gtk:en}able-pinentry-gtk \
	--%{!?with_gtk2:dis}%{?with_gtk2:en}able-pinentry-gtk2 \
	--%{!?with_qt:dis}%{?with_qt:en}able-pinentry-qt \
	--with-qt-includes=/usr/include/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/pinentry-curses
%{_infodir}/pinentry.info*

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-gtk
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-gtk-2
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt
%endif
