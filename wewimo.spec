Summary:	WeWiMo is a small script for monitoring computers connected to access point.
Summary(pl):	WeWiMo jest to ma³y skrypt do monitorowania komputerów po³±czonych do access pointa.
Name:		wewimo
Version:	0.1.0
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.mobilnews.cz/honza/dnload/wewimo//%{name}-%{version}.tar.gz
# Source0-md5:	42f78859932d433b61c9c0d96c9a45d3
URL:		http://www.mobilnews.cz/honza/en_prog_linux_wewimo.php
PreReq:		webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WeWiMo (Web WiFi Monitor) is a small script for monitoring computers
connected to access point running Linux and hostap driver for WiFi
cards (ZCom XI-626).

%description -l pl
WeWiMo (Web WiFi Monitor) jest to ma³y skrypt do monitorowania
komputerów po³±czonych do access pointa dzia³aj±cego pod kontrol±
Linuksa i u¿ywaj±cego kart WiFi (ZCom XI-626) .

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wewimo/wewimo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO INSTALL LICENSE README ChangeLog
%attr(755,root,root) %{_bindir}/*
