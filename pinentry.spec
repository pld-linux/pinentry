
#
# todo:
# - packages with Gtk+ and Qt PIN entry dialogs
#

Summary:	Simple PIN or passphrase entry dialogs
Name:		pinentry
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
URL:		http://www.gnupg.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/ncurses"
export CPPFLAGS
%configure \
	--disable-pinentry-gtk \
	--disable-pinentry-qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
