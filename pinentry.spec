# TODO: TQt dialog [BR: pkgconfig(tqt) or pkgconfig(tqt-mt), tqmoc tool]
#
# Conditional build:
%bcond_with	efl		# EFL dialog
%bcond_without	fltk		# FLTK dialog
%bcond_without	gtk2		# GTK+ 2 dialog
%bcond_without	gnome3		# GNOME 3 dialog
%bcond_without	qt4		# Qt4 dialog
%bcond_without	qt5		# Qt5 dialog
%bcond_without	qt6		# Qt6 dialog
%bcond_without	kde		# additional KDE-dependent functionality in Qt dialogs (Caps Lock detection/window parenting)
#
Summary:	Simple PIN or passphrase entry dialogs
Summary(pl.UTF-8):	Proste kontrolki dialogowe do wpisywania PIN-ów lub haseł
Name:		pinentry
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://www.gnupg.org/ftp/gcrypt/pinentry/%{name}-%{version}.tar.bz2
# Source0-md5:	5247373d2e9ac73b1ea662bd270e58a4
Patch0:		%{name}-info.patch
URL:		https://www.gnupg.org/
%{?with_qt5:BuildRequires:	Qt5Core-devel >= 5.0.0}
%{?with_qt5:BuildRequires:	Qt5Gui-devel >= 5.0.0}
%{?with_qt5:BuildRequires:	Qt5Widgets-devel >= 5.0.0}
%{?with_qt5:BuildRequires:	Qt5X11Extras-devel >= 5.1.0}
%{?with_qt6:BuildRequires:	Qt6Core-devel >= 6.4.0}
%{?with_qt6:BuildRequires:	Qt6Gui-devel >= 6.4.0}
%{?with_qt6:BuildRequires:	Qt6Widgets-devel >= 6.4.0}
%{?with_qt4:BuildRequires:	QtCore-devel >= 4}
%{?with_qt4:BuildRequires:	QtGui-devel >= 4}
%{?with_efl:BuildRequires:	elementary-devel >= 1.18}
%{?with_fltk:BuildRequires:	fltk-devel >= 1.3}
BuildRequires:	gettext-tools
%{?with_gnome3:BuildRequires:	gcr4-devel >= 4}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_qt5:%{?with_kde:BuildRequires:	kf5-kwayland-devel >= 5.91}}
# not available in PLD yet
#%{?with_qt6:%{?with_kde:BuildRequires:	kf6-kguiaddons-devel >= 5.240}}
#%{?with_qt6:%{?with_kde:BuildRequires:	kf6-kwindowsystem-devel >= 5.240}}
BuildRequires:	libassuan-devel >= 1:2.1.0
BuildRequires:	libcap-devel
BuildRequires:	libgpg-error-devel >= 1.16
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_qt4:BuildRequires:	qt4-build}
%{?with_qt5:BuildRequires:	qt5-build}
%{?with_qt6:BuildRequires:	qt6-build}
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
%{?with_kde:Requires:	kf5-kwayland >= 5.60}
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description qt5
Simple PIN or passphrase entry dialog for Qt5.

%description qt5 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt5.

%package qt6
Summary:	Simple PIN or passphrase entry dialog for Qt6
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt6
Group:		X11/Applications
Requires:	Qt6Core >= 6.4.0
Requires:	Qt6Gui >= 6.4.0
Requires:	Qt6Widgets >= 6.4.0
#%{?with_kde:Requires:	kf6-kguiaddons >= 5.240}
#%{?with_kde:Requires:	kf6-kwindowsystem >= 5.240}
Requires:	libassuan >= 1:2.1.0
Requires:	libgpg-error >= 1.16

%description qt6
Simple PIN or passphrase entry dialog for Qt6.

%description qt6 -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt6.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e 's@^\(Exec=.*/pinentry-qt\)$@\16@' qt/org.gnupg.pinentry-qt.desktop.in

%if 0
cd qt4
%{_bindir}/moc-qt4 pinentrydialog.h  -o pinentrydialog.moc
%{_bindir}/moc-qt4 pinentryconfirm.h -o pinentryconfirm.moc
%{_bindir}/moc-qt4 qsecurelineedit.h -o qsecurelineedit.moc
cd ..
%endif

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"

%configure \
	--disable-libsecret \
	--enable-fallback-curses \
	--enable-pinentry-curses \
	--enable-pinentry-efl%{!?with_efl:=no} \
	--enable-pinentry-emacs \
	--enable-pinentry-fltk%{!?with_fltk:=no} \
	--enable-pinentry-gnome3%{!?with_gnome3:=no} \
	--enable-pinentry-gtk2%{!?with_gtk2:=no} \
	--enable-pinentry-qt%{!?with_qt6:=no} \
	--enable-pinentry-qt4%{!?with_qt4:=no} \
	--enable-pinentry-qt5%{!?with_qt5:=no} \
	--enable-pinentry-tty

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%if %{with qt6}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/pinentry-qt{,6}
%{__mv} $RPM_BUILD_ROOT%{_desktopdir}/org.gnupg.pinentry-qt{,6}.desktop
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
elif [ -x %{_bindir}/pinentry-qt6 ]; then
	exec %{_bindir}/pinentry-qt6 "$@"
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
%if %{with qt5} || %{with qt6}
%{_pixmapsdir}/pinentry.png
%endif
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
%{_desktopdir}/org.gnupg.pinentry-qt5.desktop
%endif

%if %{with qt6}
%files qt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt6
%{_desktopdir}/org.gnupg.pinentry-qt6.desktop
%endif
