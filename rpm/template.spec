Name:           ros-melodic-rc-genicam-api
Version:        2.2.2
Release:        1%{?dist}
Summary:        ROS rc_genicam_api package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-melodic-catkin
BuildRequires:  cmake
BuildRequires:  libusbx

%description
GenICam/GigE Vision Convenience Layer. This package combines the Roboception
convenience layer for images with the GenICam reference implementation and a
GigE Vision transport layer. It is a self contained package that permits
configuration and image streaming of GenICam / GigE Vision 2.0 compatible
cameras like the Roboception rc_visard. This package also provides some tools
that can be called from the command line for discovering cameras, changing their
configuration and streaming images. Although the tools are meant to be useful
when working in a shell or in a script, their main purpose is to serve as
example on how to use the API for reading and setting parameters, streaming and
synchronizing images. See LICENSE.md for licensing terms of the different parts.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jul 24 2019 Felix Ruess <felix.ruess@roboception.de> - 2.2.2-1
- Autogenerated by Bloom

* Mon May 20 2019 Felix Ruess <felix.ruess@roboception.de> - 2.2.0-1
- Autogenerated by Bloom

* Mon Feb 04 2019 Felix Ruess <felix.ruess@roboception.de> - 2.1.0-0
- Autogenerated by Bloom

* Wed Jan 02 2019 Felix Ruess <felix.ruess@roboception.de> - 2.0.2-0
- Autogenerated by Bloom

* Wed Oct 24 2018 Felix Ruess <felix.ruess@roboception.de> - 2.0.0-0
- Autogenerated by Bloom

* Tue Jul 24 2018 Felix Ruess <felix.ruess@roboception.de> - 1.3.12-0
- Autogenerated by Bloom

* Mon Jul 02 2018 Felix Ruess <felix.ruess@roboception.de> - 1.3.11-0
- Autogenerated by Bloom

* Wed Apr 18 2018 Felix Ruess <felix.ruess@roboception.de> - 1.3.8-0
- Autogenerated by Bloom

* Mon Mar 19 2018 Felix Ruess <felix.ruess@roboception.de> - 1.3.6-0
- Autogenerated by Bloom

