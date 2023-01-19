%global goipath github.com/cilium/cilium-cli
Version: 0.12.12

%gometa

%global commit0 39071f6226f2b91d3599b801760300e393d683b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: cilium-cli
Release: 1%{?dist}
Summary: CLI to install, manage & troubleshoot Kubernetes clusters running Cilium
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
LDFLAGS="-X github.com/cilium/cilium-cli/internal/cli/cmd.Version=%{version} "
%gobuild -o %{gobuilddir}/bin/cilium %{goipath}/cmd/cilium

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md CODEOWNERS CODE_OF_CONDUCT.md RELEASE.md SECURITY.md
%{_bindir}/*

%changelog
* Wed Jan 11 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.12.12-1
- Bump to 0.12.12
* Sat Jan 07 2023 Karel Van Hecke <copr@karelvanhecke.com> - 0.12.11-1
- Initial build
