%def_without check

%define oname constantly
Name: python3-module-%oname
Version: 23.10.4
Release: alt1

Summary: Symbolic constants in Python

Url: http://github.com/twisted/constantly
License: X11
Group: Development/Python3
BuildArch: noarch

# https://github.com/twisted/constantly.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %oname

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.

%prep
%setup

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%{pyproject_distinfo %oname}/

%changelog
* Mon Jan 22 2024 Alexandr Sinelnikov <sasha@altlinux.org> 23.10.4-alt1
- NMU: updated to latest release.

* Sun Jan 21 2024 Alexandr Sinelnikov <sasha@altlinux.org> 15.1.0-alt7
- NMU: fixed FTBFS (configparser deprecation).

* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt6
- Build without python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 15.1.0-alt5.qa1
- NMU: applied repocop patch

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt5
- Updated build dependencies.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt4
- Fixed egg-info version.
- Explicitely stated egg-info including valid version.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt3
- Fixed egg-info version.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt2
- Enabled build for python-3.

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt1
- initial build for ALT Sisyphus

