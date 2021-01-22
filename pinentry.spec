# TODO: TQt dialog [BR: pkgconfig(tqt) or pkgconfig(tqt-mt), tqmoc tool]
#
# Conditional build:
%bcond_with	efl	# EFL dialog
%bcond_without	fltk	# FLTK dialog
%bcond_without	gtk2	# GTK+ 2 dialog
%bcond_without	gnome3	# GNOME 3 dialog
%bcond_without	qt4	# Qt4 dialog
%bcond_without	qt5	# Qt5 dialog
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl.UTF-8):	Proste kontrolki dialogowe do wpisywania PIN-ów lub haseł
Name:		pinentry
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2
# Source0-md5:	d7f646d373b722317d985cddc1d107c1
Patch0:		%{name}-info.patch
Patch1:		%{name}-am.patch
URL:		http://www.gnupg.org/
%{?with_qt5:BuildRequires:	Qt5Core-devel >= 5}
%{?with_qt5:BuildRequires:	Qt5Gui-devel >= 5}
%{?with_qt5:BuildRequires:	Qt5Widgets-devel >= 5}
%{?with_qt4:BuildRequires:	QtCore-devel >= 4}
%{?with_qt4:BuildRequires:	QtGui-devel >= 4}
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
%{?with_efl:BuildRequires:	elementary-devel >= 1.18}
%{?with_fltk:BuildRequires:	fltk-devel >= 1.3}
BuildRequires:	gettext-tools
%{?with_gnome3:BuildRequires:	gcr-devel >= 3}
%{?with_gnome3:BuildRequires:	gcr-ui-devel >= 3}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
BuildRequires:	libassuan-devel >= 1:2.1.0
BuildRequires:	libcap-devel
BuildRequires:	libgpg-error-devel >= 1.16
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_qt4:BuildRequires:	qt4-build}
%{?with_qt5:BuildRequires:	qt5-build}
BuildRequires:	texinfo
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16
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

%package emacs
Summary:	Simple PIN or passphrase entry dialog for Emacs
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Emacsa
Group:		Applications
Requires:	emacs
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description emacs
Simple PIN or passphrase entry dialog for Emacs.

%description emacs -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Emacsa.

%package efl
Summary:	Simple PIN or passphrase entry dialog using EFL
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł wykorzystująca bibliotekę EFL
Group:		X11/Applications
Requires:	elementary-libs >= 1.18
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description efl
Simple PIN or passphrase entry dialog using EFL.

%description efl -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł
wykorzystująca bibliotekę EFL.

%package fltk
Summary:	Simple PIN or passphrase entry dialog using FLTK
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł wykorzystująca bibliotekę FLTK
Group:		X11/Applications
Requires:	fltk >= 1.3
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description fltk
Simple PIN or passphrase entry dialog using FLTK.

%description fltk -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł
wykorzystująca bibliotekę FLTK.

%package gnome3
Summary:	Simple PIN or passphrase entry dialog for GNOME 3
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GNOME 3
Group:		X11/Applications
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description gnome3
Simple PIN or passphrase entry dialog for GNOME 3.

%description gnome3 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GNOME 3.

%package gtk2
Summary:	Simple PIN or passphrase entry dialog for GTK+ 2
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2
Group:		X11/Applications
Requires:	gtk+2 >= 2:2.12.0
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description gtk2
Simple PIN or passphrase entry dialog for GTK+ 2.

%description gtk2 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 2.

%package qt4
Summary:	Simple PIN or passphrase entry dialog for Qt4
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt4
Group:		X11/Applications
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description qt4
Simple PIN or passphrase entry dialog for Qt4.

%description qt4 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt4.

%package qt5
Summary:	Simple PIN or passphrase entry dialog for Qt5
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt5
Group:		X11/Applications
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description qt5
Simple PIN or passphrase entry dialog for Qt5.

%description qt5 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%if 0
cd qt4
%{_bindir}/moc-qt4 pinentrydialog.h  -o pinentrydialog.moc
%{_bindir}/moc-qt4 pinentryconfirm.h -o pinentryconfirm.moc
%{_bindir}/moc-qt4 qsecurelineedit.h -o qsecurelineedit.moc
cd ..
%endif

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"

mkdir build
cd build
../%configure \
	--enable-maintainer-mode \
	--disable-libsecret \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--enable-pinentry-efl%{!?with_efl:=no} \
	--enable-pinentry-emacs \
	--enable-pinentry-fltk%{!?with_fltk:=no} \
	--enable-pinentry-gnome3%{!?with_gnome3:=no} \
	--enable-pinentry-gtk2%{!?with_gtk2:=no} \
	--enable-pinentry-qt%{!?with_qt5:=no} \
	--enable-pinentry-tty

%{__make}
cd ..

%if %{with qt4}
install -d build-qt4
# hack: avoid qt5 detection so configure fallbacks to qt4
%{__mv} configure configure.orig
%{__sed} -e 's/Qt5Core/Qt999Core/' configure.orig > configure
chmod +x configure
cd build-qt4
../%configure \
	--enable-maintainer-mode \
	--disable-libsecret \
	--enable-fallback-curses \
	--disable-pinentry-curses \
	--disable-pinentry-emacs \
	--disable-pinentry-gnome3 \
	--disable-pinentry-gtk2 \
	--enable-pinentry-qt \
	--disable-pinentry-tty
%{__make}
cd ..
%{__mv} configure.orig configure
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pinentry-qt{,4}
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT
%if %{with qt5}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pinentry-qt{,5}
%endif

%{__rm} $RPM_BUILD_ROOT%{_bindir}/pinentry
cat >$RPM_BUILD_ROOT%{_bindir}/pinentry <<'EOF'
#!/bin/sh

if [ -n "$PINENTRY_PROGRAM" ]; then
	exec $PINENTRY_PROGRAM "$@"
elif [ -z "$DISPLAY" ]; then
	exec %{_bindir}/pinentry-curses "$@"
elif [ -x %{_bindir}/pinentry-gnome3 ]; then
	exec %{_bindir}/pinentry-gnome3 "$@"
elif [ -x %{_bindir}/pinentry-gtk-2 ]; then
	exec %{_bindir}/pinentry-gtk-2 "$@"
elif [ -x %{_bindir}/pinentry-gtk ]; then
	exec %{_bindir}/pinentry-gtk "$@"
elif [ -x %{_bindir}/pinentry-qt5 ]; then
	exec %{_bindir}/pinentry-qt5 "$@"
elif [ -x %{_bindir}/pinentry-qt4 ]; then
	exec %{_bindir}/pinentry-qt4 "$@"
elif [ -x %{_bindir}/pinentry-qt ]; then
	exec %{_bindir}/pinentry-qt "$@"
elif [ -x %{_bindir}/pinentry-fltk ]; then
	exec %{_bindir}/pinentry-fltk "$@"
elif [ -x %{_bindir}/pinentry-efl ]; then
	exec %{_bindir}/pinentry-efl "$@"
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

%if %{with efl}
%files efl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-efl
%endif

%files emacs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-emacs

%if %{with fltk}
%files fltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-fltk
%endif

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

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt5
%endif
