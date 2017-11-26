%define _topdir %(pwd)

name:      SoapUI
version:   5.3.0
release:   1
summary:   SoapUI
license:   EUPL, Version 1.1+
group:     Development/Tools
vendor:    SmartBear
url:       https://www.soapui.org/downloads/latest-release.html
source:    %{name}-%{version}-linux-bin.tar.gz
source1:   SoapUI.png
patch0:    logroot.patch
buildarch: noarch
requires:  jre

%description
SoapUI.

%prep

%setup -q
%patch0 -p1
cp %{SOURCE1} .

%install

mkdir -p %{buildroot}/opt/%{vendor}/%{name}-%{version}
mv %{_builddir}/%{name}-%{version}/* %{buildroot}/opt/%{vendor}/%{name}-%{version}/

cat <<__EOF >%{buildroot}/opt/%{vendor}/%{name}-%{version}/%{vendor}-%{name}.desktop
[Desktop Entry]
Name=Soap UI
Exec=/opt/%{vendor}/%{name}-%{version}/bin/soapui.sh %f
Terminal=false
Icon=/opt/%{vendor}/%{name}-%{version}/SoapUI.png
Type=Application
Categories=Development
__EOF

%post
/usr/bin/xdg-desktop-menu install /opt/%{vendor}/%{name}-%{version}/%{vendor}-%{name}.desktop

%preun
[ $1 = 0 ] && /usr/bin/xdg-desktop-menu uninstall /opt/%{vendor}/%{name}-%{version}/%{vendor}-%{name}.desktop

%files
%dir /opt/%{vendor}
/opt/%{vendor}/%{name}-%{version}
