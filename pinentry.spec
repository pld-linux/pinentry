# TODO: use system libassuan 2 instead of included libassuan 1
#
# Conditional build:
%bcond_without	gtk2	# without GTK+ 2 dialog
%bcond_without	gnome3	# without GNOME 3 dialog
%bcond_without	qt4	# without Qt4 dialog
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl.UTF-8):	Proste kontrolki dialogowe do wpisywania PIN-ów lub haseł
Name:		pinentry
Version:	0.9.4
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2
# Source0-md5:	50dd255d23839079e15a02761f11d4c8
Patch0:		%{name}-system-assuan.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-am.patch
URL:		http://www.gnupg.org/
%{?with_qt4:BuildRequires:	QtCore-devel >= 4}
%{?with_qt4:BuildRequires:	QtGui-devel >= 4}
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	gettext-tools
%{?with_gnome3:BuildRequires:	gcr-devel >= 3}
%{?with_gnome3:BuildRequires:	gcr-ui-devel >= 3}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.4.0}
#BuildRequires:	libassuan-devel
BuildRequires:	libcap-devel
BuildRequires:	libsecret-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_qt4:BuildRequires:	qt4-build}
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

%package gnome3
Summary:	Simple PIN or passphrase entry dialog for GNOME 3
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GNOME 3
Group:		X11/Applications
Requires:	gtk+2 >= 2:2.4.0

%description gnome3
Simple PIN or passphrase entry dialog for GNOME 3.

%description gnome3 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GNOME 3.

%package gtk2
Summary:	Simple PIN or passphrase entry dialog for GTK+ 2
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2
Group:		X11/Applications
Requires:	gtk+2 >= 2:2.4.0

%description gtk2
Simple PIN or passphrase entry dialog for GTK+ 2.

%description gtk2 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2.

%package qt4
Summary:	Simple PIN or passphrase entry dialog for Qt4
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt4
Group:		X11/Applications

%description qt4
Simple PIN or passphrase entry dialog for Qt4.

%description qt4 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt4.

%prep
%setup -q
#patch0 -p1
%patch1 -p1
%patch2 -p1

%if %{with qt4}
cd qt4
%{_bindir}/moc-qt4 pinentrydialog.h  -o pinentrydialog.moc
%{_bindir}/moc-qt4 pinentryconfirm.h -o pinentryconfirm.moc
%{_bindir}/moc-qt4 qsecurelineedit.h -o qsecurelineedit.moc
cd ..
%endif

#%{__rm} assuan/*.h

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--enable-maintainer-mode \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--enable-pinentry-gnome3%{!?with_gnome3:=no} \
	--enable-pinentry-gtk2%{!?with_gtk2:=no} \
	--enable-pinentry-qt4%{!?with_qt4:=no} \
	--enable-pinentry-tty

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/pinentry
cat >$RPM_BUILD_ROOT%{_bindir}/pinentry <<'EOF'
#!/bin/sh

if [ -n "$PINENTRY_PROGRAM" ]; then
	exec $PINENTRY_PROGRAM "$@"
elif [ -z "$DISPLAY" ]; then
	exec %{_bindir}/pinentry-curses "$@"
elif [ -x %{_bindir}/pinentry-gtk-2 ]; then
	exec %{_bindir}/pinentry-gtk-2 "$@"
elif [ -x %{_bindir}/pinentry-gtk ]; then
	exec %{_bindir}/pinentry-gtk "$@"
elif [ -x %{_bindir}/pinentry-qt4 ]; then
	exec %{_bindir}/pinentry-qt4 "$@"
elif [ -x %{_bindir}/pinentry-qt ]; then
	exec %{_bindir}/pinentry-qt "$@"
else
	exec %{_bindir}/pinentry-curses "$@"
fi
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/pinentry
%attr(755,root,root) %{_bindir}/pinentry-curses
%attr(755,root,root) %{_bindir}/pinentry-tty
%{_infodir}/pinentry.info*

%if %{with gnome3}
%files gnome3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-gnome3
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-gtk-2
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt4
%endif
