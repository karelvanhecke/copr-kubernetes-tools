%global goipath github.com/cilium/hubble
Version: 0.11.1

%gometa

%global commit0 9d483eb60ec71a2358c3d513af75f3761a7832e2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: hubble
Release: 1%{?dist}
Summary: Hubble - Network, Service & Security Observability for Kubernetes using eBPF
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
LDFLAGS="-X github.com/cilium/hubble/pkg.GitBranch=master \
-X github.com/cilium/hubble/pkg.GitHash=%{shortcommit0} \
-X github.com/cilium/hubble/pkg.Version=%{version} "
%gobuild -o %{gobuilddir}/bin/hubble %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md CHANGELOG.md CODEOWNERS CONTRIBUTING.md RELEASE.md
%{_bindir}/*

%changelog
* Fri Jan 27 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.11.1-1
- Bump to 0.11.1
* Thu Jan 12 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.11.0-1
- Bump to 0.11.0
* Sat Jan 07 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.10.0-1
- Initial build
