#
# Conditional build:
%bcond_without	gtk	# without GTK+ dialog
%bcond_without	qt	# without Qt dialog
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl):	Proste kontrolki dialogowe do wpisywania PIN-ów lub hase³
Name:		pinentry
Version:	0.7.1
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.gz
# Source0-md5:	7861d63dea6434a5a05da84e83f209e6
Patch0:		%{name}-system-assuan.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7.6
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
BuildRequires:	libassuan-devel >= 1:0.6.0
BuildRequires:	libcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
%{?with_qt:BuildRequires:	qt-devel}
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

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--enable-maintainer-mode \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--%{!?with_gtk:dis}%{?with_gtk:en}able-pinentry-gtk \
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

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt
%endif
