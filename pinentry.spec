
#
# todo:
# - packages with Gtk+ and Qt PIN entry dialogs
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

%description -l pl
Jest to zestaw prostych kontrolek dialogowych do wpisywania PIN-ów lub
hase³, u¿ywaj±ce protoko³u Assuan opisanego w projekcie aegypten;
wiêcej szczegu³ów pod adresem http://www.gnupg.org/aegypten/.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
CPPFLAGS="-I/usr/include/ncurses"
export CPPFLAGS
%configure \
	--enable-maintainer-mode \
	--disable-pinentry-gtk \
	--disable-pinentry-qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_infodir}/pinentry.info*
