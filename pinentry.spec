#
# Conditional build:
# _without_gtk	- without GTK+ dialog
# _without_qt	- without Qt dialog
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl):	Proste kontrolki dialogowe do wpisywania PIN-ów lub hase³
Name:		pinentry
Version:	0.6.8
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
Patch0:		%{name}-cxx.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.5
%{!?_without_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
BuildRequires:	libcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
%{!?_without_qt:BuildRequires:	qt-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details. Base package contains
curses-based dialog.

%description -l pl
Jest to zestaw prostych kontrolek dialogowych do wpisywania PIN-ów lub
hase³, u¿ywaj±ce protoko³u Assuan opisanego w projekcie aegypten;
wiêcej szczegó³ów pod adresem http://www.gnupg.org/aegypten/.
Podstawowy pakiet zawiera kontrolkê opart± na curses.

%package gtk
Summary:	Simple PIN or passphrase entry dialog for GTK+
Summary(pl):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub hase³ dla GTK+
Group:		X11/Applications

%description gtk
Simple PIN or passphrase entry dialog for GTK+.

%description gtk -l pl
Prosta kontrolka dialogowa do wpisywania PIN-ów lub hase³ dla GTK+.

%package qt
Summary:	Simple PIN or passphrase entry dialog for Qt
Summary(pl):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub hase³ dla Qt
Group:		X11/Applications

%description qt
Simple PIN or passphrase entry dialog for Qt.

%description qt -l pl
Prosta kontrolka dialogowa do wpisywania PIN-ów lub hase³ dla Qt.

%package -n libassuan-devel
Summary:	Assuan protocol static library
Summary(pl):	Statyczna biblioteka obs³uguj±ca protokó³ Assuan
Group:		Development/Libraries

%description -n libassuan-devel
Assuan protocol static library.

%description -n libassuan-devel -l pl
Statyczna biblioteka obs³uguj±ca protokó³ Assuan.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--enable-maintainer-mode \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--%{?_without_gtk:dis}%{!?_without_gtk:en}able-pinentry-gtk \
	--%{?_without_qt:dis}%{!?_without_qt:en}able-pinentry-qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
install assuan/libassuan.a $RPM_BUILD_ROOT%{_libdir}

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

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-gtk

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt

%files -n libassuan-devel
%defattr(644,root,root,755)
%{_libdir}/libassuan.a
