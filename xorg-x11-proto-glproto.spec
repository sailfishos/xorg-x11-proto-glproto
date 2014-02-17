# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       xorg-x11-proto-glproto

# >> macros
# << macros

Summary:    X.Org X11 Protocol glproto
Version:    1.4.17
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/glproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-glproto.yaml
Provides:   glproto

%description
glproto is the protocol for the client to send 3D rendering commands to the X server.

%prep
%setup -q -n glproto-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/pkgconfig/glproto.pc
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxtokens.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%{_includedir}/GL/glxint.h
# << files
