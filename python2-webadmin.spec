%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define proj_name webadmin

%define _release RELEASEVERSION

Name:           python-%{proj_name}
Version:        RPMVERSION
Release:        %{_release}%{?dist}
Summary:        xiaochen go game operation
Group:          Development/Libraries
License:        MPLv1.1 or GPLv2
URL:            http://github.com/Lolizeppelin/%{proj_name}
Source0:        %{proj_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools >= 11.3

Requires:       python >= 2.6.6
Requires:       python < 3.0
Requires:       python-goperation >= 1.0
Requires:       python-goperation < 1.1


%description
A webadmin test web

%prep
%setup -q -n %{proj_name}-%{version}
rm -rf %{proj_name}.egg-info

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
install -d %{buildroot}%{_sysconfdir}/goperation/endpoints
install -p -D -m 0644 etc/endpoints/*.conf.sample %{buildroot}%{_sysconfdir}/goperation/endpoints

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_bindir}
install -p -D -m 0754 sbin/* %{buildroot}%{_sbindir}
#install -p -D -m 0755 bin/* %{buildroot}%{_bindir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/%{proj_name}/*.py
%{python_sitelib}/%{proj_name}/*.pyc
%{python_sitelib}/%{proj_name}/*.pyo
%{python_sitelib}/%{proj_name}/api/*.py
%{python_sitelib}/%{proj_name}/api/*.pyc
%{python_sitelib}/%{proj_name}/api/*.pyo
%{python_sitelib}/%{proj_name}/api/client
%{python_sitelib}/%{proj_name}/cmd
%{python_sitelib}/%{proj_name}-%{version}-py?.?.egg-info
%{_sbindir}/gop%{proj_name}-init
#%doc README.md
#%doc doc/*


%package server
Summary:        webadmin wsgi server
Group:          Development/Libraries
Requires:       %{name} == %{version}
Requires:       python-goperation-server >= 1.0
Requires:       python-goperation-server < 1.1

%description server
webadmin wsgi routes

%files server
%defattr(-,root,root,-)
%dir %{python_sitelib}/%{proj_name}/api/wsgi
%{python_sitelib}/%{proj_name}/api/wsgi/*
%{_sysconfdir}/goperation/endpoints/webadmin.server.conf.sample

%changelog

* Mon Aug 29 2017 Lolizeppelin <lolizeppelin@gmail.com> - 1.0.0
- Initial Package