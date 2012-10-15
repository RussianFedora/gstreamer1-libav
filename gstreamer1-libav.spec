Summary:	Gstreamer plugin for the libav codec
Name:		gstreamer1-libav
Version:	1.0.1
Release:	1%{?dist}

Source0:	http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://gstreamer.freedesktop.org

Provides:	gstreamer1-ffmpeg = %{version}-%{release}
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	orc-devel
BuildRequires:	freetype-devel
BuildRequires:	check-devel
Buildrequires:	yasm
BuildRequires: bzip2-devel

%description
Video codec plugin for GStreamer based on the libav libraries.

%prep
%setup -q -n gst-libav-%version

%build
%configure \
  --disable-static \
  --with-package-name='%{distribution} %name package' \
  --with-package-origin='http://www.mageia.org/' \
  --with-libav-extra-configure='--disable-decoder=mp3 --disable-decoder=mp3on4 --disable-decoder=mp3adu --disable-demuxer=mp3 --disable-demuxer=asf'
make

%install
%makeinstall

find %{buildroot} -name '*.la' -delete

%files
%defattr(-,root,root,-)
%doc README NEWS TODO ChangeLog AUTHORS 
%{_libdir}/gstreamer-1.0/libgstlibav.so
%{_libdir}/gstreamer-1.0/libgstavscale.so


%changelog

* Mon Oct 08 2012 fwang <fwang> 1.0.1-1.mga3
+ Revision: 303339
- new version 1.0.0

* Mon Sep 24 2012 fwang <fwang> 1.0.0-1.mga3
+ Revision: 297089
- update br
- new version 1.0.0

* Tue Sep 18 2012 fwang <fwang> 0.11.99-1.mga3
+ Revision: 295772
- new version 0.11.99

* Mon Sep 17 2012 fwang <fwang> 0.11.94-1.mga3
+ Revision: 294773
- update file list
- new version 0.11.94

* Wed Sep 05 2012 fwang <fwang> 0.11.93-1.mga3
+ Revision: 288521
- update file list
- rename to libav
- rename package
- the code now is based on libav rather than ffmpeg
- update provides
- imported package gstreamer1.0-ffmpeg

