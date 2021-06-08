Name:       libxkbcommon

Summary:    Xorg X11 common xkb library
Version:    0.3.2
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    libxkbcommon-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  byacc
BuildRequires:  libtool
BuildRequires:  flex
BuildRequires:  bison

%description
xkb Libraries file.

%package devel
Summary:    Xorg X11 common xkb libray
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
xkb Development Libraries file.


%prep
%setup -q -n %{name}-%{version}/%{name}


%build

CFLAGS="-std=c99" %autogen --disable-static \
    --with-xkb-config-root=/usr/share/X11/xkb

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libxkbcommon.so.0
%{_libdir}/libxkbcommon.so.0.0.0

%files devel
%defattr(-,root,root,-)
#%{_libdir}/extensions/XKBcommon.h
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_libdir}/libxkbcommon.so
%{_libdir}/pkgconfig/xkbcommon.pc
