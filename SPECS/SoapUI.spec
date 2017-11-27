%define _topdir %(pwd)
%define product_name    SoapUI
%define product_version 5.3
%define product_patch   0
%define product_dir      %{product_name}-%{version}.%{product_patch}

name:      %{product_name}%{product_version}
version:   %{product_version}
release:   %{product_patch}.1
summary:   SoapUI
license:   EUPL, Version 1.1+
group:     Development/Tools
vendor:    SmartBear
url:       https://www.soapui.org/downloads/latest-release.html
source:    %{product_name}-%{version}.%{product_patch}-linux-bin.tar.gz
source1:   SoapUI.png
patch0:    logroot.patch
buildarch: noarch
requires:  jre >= 1.7

%description
SoapUI.

%prep

%setup -q -n %{product_dir}
%patch0 -p1
cp %{SOURCE1} .

%install

mkdir -p %{buildroot}/opt/%{vendor}/%{name}
mv %{_builddir}/%{product_dir}/* %{buildroot}/opt/%{vendor}/%{name}/

cat <<__EOF >%{buildroot}/opt/%{vendor}/%{name}/%{vendor}-%{name}.desktop
[Desktop Entry]
Name=SoapUI %{version}
Exec=/opt/%{vendor}/%{name}/bin/soapui.sh %f
Terminal=false
Icon=/opt/%{vendor}/%{name}/SoapUI.png
Type=Application
Categories=Development
__EOF

%post
/usr/bin/xdg-desktop-menu install /opt/%{vendor}/%{name}/%{vendor}-%{name}.desktop

%preun
[ $1 = 0 ] && /usr/bin/xdg-desktop-menu uninstall /opt/%{vendor}/%{name}/%{vendor}-%{name}.desktop

%files
%dir /opt/%{vendor}
/opt/%{vendor}/%{name}
